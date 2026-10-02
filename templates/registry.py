"""V2 manifest-driven template registry.

The catalog starts empty until a new template is intentionally released.
Legacy clone implementations are not registered here.
"""

from dataclasses import dataclass, field
from typing import Sequence


@dataclass(frozen=True, slots=True)
class TemplateCommand:
    command: str
    description: str


@dataclass(frozen=True, slots=True)
class TemplatePricing:
    mode: str = "free"  # free | coins | upi | redeem | referral
    coin_price: int = 0
    inr_price: int = 0


@dataclass(frozen=True, slots=True)
class TemplateManifest:
    slug: str
    name: str
    description: str
    category: str
    version: str
    commands: Sequence[TemplateCommand] = field(default_factory=tuple)
    pricing: TemplatePricing = field(default_factory=TemplatePricing)
    enabled: bool = True


# New V2 templates are registered here as they are released.
TEMPLATES: dict[str, TemplateManifest] = {}


def get_template(slug: str) -> TemplateManifest | None:
    return TEMPLATES.get(slug)


def available_templates() -> tuple[TemplateManifest, ...]:
    return tuple(template for template in TEMPLATES.values() if template.enabled)


def register_template(template: TemplateManifest) -> None:
    if template.slug in TEMPLATES:
        raise ValueError(f"Template already registered: {template.slug}")
    TEMPLATES[template.slug] = template
