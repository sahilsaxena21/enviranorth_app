# Frontmatter Templates

Every wiki file must have YAML frontmatter. Use the appropriate template for its type.

> **What is a slug?** A slug is the filename without the folder path or `.md` extension. For example, the slug for `controls/smartair.md` is `smartair`. Slugs are used in frontmatter fields like `controls_compatible`, `works_with`, `applies_to`, and `compares` to link files together.

## Product
```yaml
---
id: {slug}
sku: {SKU}
name: {Full product name}
type: product
product_line: {line name}
drive: {gearmotor|direct-drive|brushless-dc|ec-motor|passive}
categories: [hvls, spot-cooling, ventilation, ...]
applications: [warehouse, dairy-barn, ...]
related: [other-product-slug, ...]
controls_compatible: [control-slug, ...]
source_docs:
  - "{exact filename from raw_text/}"
last_verified: YYYY-MM-DD
---
```

## Control
```yaml
---
id: {slug}
name: {Full name}
type: control
category: {vfd-package|hmi|zone-controller|sensor|relay}
vfd: {brand — Schneider|Lenze|n/a}
location: {fan-mounted|wall-mounted|panel}
fans_controlled: {1|"up to 10"|"up to 20"}
works_with: [product-slug, ...]
source_docs:
  - "{exact filename from raw_text/}"
last_verified: YYYY-MM-DD
---
```

## Comparison
```yaml
---
id: {slug}
name: {Title}
type: comparison
compares: [slug-a, slug-b, ...]
source_docs:
  - "{exact filename from raw_text/}"
last_verified: YYYY-MM-DD
---
```

## Application
```yaml
---
id: application-{slug}
name: {Application name}
type: application
recommended_products: [product-slug, ...]
recommended_controls: [control-slug, ...]
source_docs:
  - "{exact filename from raw_text/}"
last_verified: YYYY-MM-DD
---
```

## Guide
```yaml
---
id: {slug}
name: {Title}
type: guide
category: {electrical|mounting|maintenance|warranty}
applies_to: [product-slug, ...]
source_docs:
  - "{exact filename from raw_text/}"
last_verified: YYYY-MM-DD
---
```
