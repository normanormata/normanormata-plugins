#!/usr/bin/env python3
"""Validate marketplace, plugin, and skill metadata without dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "westminster-standards"
EXPECTED_VERSION = "0.2.1"
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
REFERENCE_PATTERN = re.compile(
    r"(?:`|\()(?P<path>references/[A-Za-z0-9._/-]+\.md)(?:`|\))"
)


class ValidationError(Exception):
    """Raised when repository metadata is inconsistent."""


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"{path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError(f"{path.relative_to(ROOT)}: expected a JSON object")
    return value


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValidationError(f"{path.relative_to(ROOT)}: missing opening frontmatter marker")
    try:
        closing = lines.index("---", 1)
    except ValueError as exc:
        raise ValidationError(
            f"{path.relative_to(ROOT)}: missing closing frontmatter marker"
        ) from exc

    metadata: dict[str, str] = {}
    for line in lines[1:closing]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValidationError(f"{path.relative_to(ROOT)}: invalid frontmatter line {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value or key in metadata:
            raise ValidationError(f"{path.relative_to(ROOT)}: invalid frontmatter key {key!r}")
        metadata[key] = value

    if set(metadata) != {"name", "description"}:
        raise ValidationError(
            f"{path.relative_to(ROOT)}: frontmatter must contain only name and description"
        )
    body = "\n".join(lines[closing + 1 :]).strip()
    if not body:
        raise ValidationError(f"{path.relative_to(ROOT)}: skill body is empty")
    return metadata, body


def validate_manifests() -> Path:
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        raise ValidationError("marketplace.json: plugins must be a list")
    matches = [entry for entry in entries if entry.get("name") == PLUGIN_NAME]
    if len(matches) != 1:
        raise ValidationError(f"marketplace.json: expected one {PLUGIN_NAME!r} entry")
    entry = matches[0]

    source = entry.get("source")
    if not isinstance(source, str) or not source.startswith("./"):
        raise ValidationError("marketplace.json: plugin source must be a relative ./ path")
    plugin_dir = (ROOT / source).resolve()
    if plugin_dir.parent != (ROOT / "plugins").resolve() or not plugin_dir.is_dir():
        raise ValidationError("marketplace.json: plugin source does not name a plugin directory")

    manifest = load_json(plugin_dir / ".claude-plugin" / "plugin.json")
    for key in ("name", "version", "description"):
        if entry.get(key) != manifest.get(key):
            raise ValidationError(f"manifest mismatch for {key!r}")
    if manifest.get("name") != PLUGIN_NAME:
        raise ValidationError(f"plugin manifest name must be {PLUGIN_NAME!r}")
    if manifest.get("version") != EXPECTED_VERSION:
        raise ValidationError(f"plugin version must be {EXPECTED_VERSION}")
    return plugin_dir


def validate_skills(plugin_dir: Path) -> int:
    skills_dir = plugin_dir / "skills"
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    if not skill_files:
        raise ValidationError("plugin contains no skills")

    for skill_file in skill_files:
        metadata, body = parse_frontmatter(skill_file)
        skill_name = metadata["name"]
        if not NAME_PATTERN.fullmatch(skill_name):
            raise ValidationError(f"{skill_file.relative_to(ROOT)}: invalid skill name")
        if skill_file.parent.name != skill_name:
            raise ValidationError(
                f"{skill_file.relative_to(ROOT)}: skill name must match its directory"
            )
        for match in REFERENCE_PATTERN.finditer(body):
            reference = skill_file.parent / match.group("path")
            if not reference.is_file():
                raise ValidationError(
                    f"{skill_file.relative_to(ROOT)}: missing {match.group('path')}"
                )
    return len(skill_files)


def main() -> int:
    try:
        plugin_dir = validate_manifests()
        skill_count = validate_skills(plugin_dir)
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"Validated {PLUGIN_NAME} {EXPECTED_VERSION}: {skill_count} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
