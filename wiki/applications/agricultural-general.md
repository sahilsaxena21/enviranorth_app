---
id: application-agricultural-general
name: Agricultural Installations — General Rules
type: application
recommended_products: [sailfin-gearless-20ft, sailfin-gearless-24ft, sailfin-geared-20ft, sailfin-geared-24ft]
recommended_controls: [smartair, smartair-multifan, touchair, lvc, tfd-1, wind-sensor]
source_docs:
  - "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
  - "HogBrochure-Sailfin-EN (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt"
  - "Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt"
last_verified: 2026-04-11
---

# Agricultural Installations — General Rules

## Overview
"Agricultural" covers dairy barns, hog finishing / farrowing, poultry houses, riding arenas, greenhouses, equestrian barns, and similar facilities. Envira-North has a set of rules that apply to **all** agricultural installs regardless of species. This page consolidates those rules. For species-specific details, see the dedicated application pages (`dairy-barn.md`, etc.).

## The three non-negotiable rules

### 1. Wind sensor is MANDATORY
- Every agricultural install must have a wind sensor
- If not installed, a factory jumper occupies its position and the fan will not operate
- Skipping this is a warranty and structural safety concern
- See `controls/wind-sensor.md` for trigger behaviour and wiring

### 2. Minimum speed is 15 Hz / 27 %
- Never program below this
- The motor overheats at lower speeds because it doesn't move enough air to self-cool
- Running below 15 Hz voids the warranty

### 3. Corrosion-appropriate hardware
- Agricultural environments are corrosive: ammonia, moisture, manure, salt (winter)
- Specify the appropriate blade and hardware finish when ordering
- Contact Envira-North Customer Support for the species-specific spec (dairy vs. hog vs. poultry)
- Do not swap generic fasteners on site

## Performance context (from Altra-Air D&E guide)
- HVLS fans create an **evaporative cooling effect of 3 to 4 degrees Celsius** throughout the facility
- De-stratifies uneven temperatures of **up to 15°C from ceiling to floor**, reducing heating system cycling
- Adequate fresh air exchange is crucial for animals to perform at their best
- **Improves air quality** by lowering impurity levels caused by animal respiration and toxic chemical/ammonia emissions
- Lowers temperatures by cooling roof spaces and removing trapped ceiling heat

## Recommended fans
- **Sailfin Gearless 20 ft / 24 ft** — large-volume coverage, lowest long-term maintenance (no gearbox oil); noise level 45 dBA — important for animal welfare
- **Sailfin Geared 20 ft / 24 ft** — lower up-front cost
- Size depends on the building — see dedicated application pages

## Recommended controls
- **SmartAIR / SmartAIR Multi-Fan** — best for agricultural because **humidity automation** matters as much as temperature (dairy, hog, poultry all have humidity-driven heat stress)
- **LVC + TFD-1** — cheaper temperature-only automation; acceptable when humidity is not a concern
- **TouchAIR** — larger operations (11–20 fans) or multi-building agricultural complexes
- **Wind Sensor** — mandatory, see above

## Environmental ratings
- Sailfin fans are rated for indoor or covered-outdoor agricultural use
- HMIs should be mounted in a dry office or control room, not in the barn proper
- If the HMI must be in a wet / wash-down area, use TouchAIR (NEMA4X)
- Jazz is indoor-only (IP54) and not typically used in barns

## Species-specific corrosion
| Species | Primary corrosion concern | Hardware note |
|---|---|---|
| Dairy | Ammonia, moisture, manure | Corrosion-resistant blades and hardware |
| Hog | Ammonia (high), moisture, manure | Heavier corrosion package — confirm with Customer Support |
| Poultry | Ammonia, dust | Similar to hog spec |
| Equestrian | Moisture, dust | Lighter spec than dairy/hog |
| Greenhouse | Moisture, fertiliser overspray | Confirm with Customer Support |

## Power
- Most agricultural facilities are on 230 V or 460 V three-phase
- Both Schneider and Lenze drives support these natively
- Confirm the voltage before ordering — 600 V is less common but supported

## Mounting
- Blade-to-floor: 10 ft minimum (measured from the lowest point of the blade to the animal's floor level, not the bedding level)
- Spacing: 2.5× diameter centre-to-centre
- Structural review is mandatory — agricultural truss and purlin structures are often lighter than industrial, so load capacity needs verification
- Open-wall and half-open-wall barns need the wind sensor mounted where it reads representative wind, not sheltered by the wall

## Maintenance schedule (agricultural)
- Standard schedule: 6 months initial inspection, then every 18 months
- Geared Sailfin: oil change every 20,000 hours, first-start vent plug removal
- Wind sensor: test the trigger before every hot season
- Clean blades and drive enclosures at each inspection — corrosive buildup is worse in agricultural than in industrial

## Common pitfalls
- Skipping wind sensor → warranty voided, fan exposed to gust damage
- Generic (non-corrosion-resistant) hardware → hardware fails in 2–3 years instead of 15+
- Running below 15 Hz "to save power at night" → motor overheats, warranty voided
- Mounting HMI in the barn without NEMA4X → moisture damage
- Ignoring the gearbox vent plug on first start-up → seal blows on first run

## Common FAQs

**Q: Which species does Envira-North specifically market to?**
A: Dairy, hog (finishing and farrowing), poultry, equestrian, and greenhouse are all explicitly in the product brochures. The same Sailfin fan works across all of them — the difference is hardware finish and control strategy.

**Q: Can I use TFD-1 in a dairy barn?**
A: You can, but you lose humidity automation. For dairy (and hog, and poultry), SmartAIR is recommended because humidity is as important as temperature for heat stress.

**Q: Is the wind sensor really required if my barn is enclosed?**
A: The rule is "all agricultural installs." Even an enclosed barn benefits from the shutdown during a severe storm when roof loading or debris could affect the fan. When in doubt, install it — it's mandatory per Envira-North.

**Q: Can I retrofit a wind sensor later?**
A: Yes — the factory jumper comes out and the sensor wires in its place. Contact Envira-North Customer Support for the retrofit kit.

**Q: Can I use Jazz fans in a barn?**
A: Not recommended — Jazz is indoor-only (IP54) and on its own network. Sailfin is the agricultural fan.

## Source Documents Referenced
- `Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt`
- `HogBrochure-Sailfin-EN (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt`
- `Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt`
