---
id: application-dairy-barn
name: Dairy Barn Application
type: application
recommended_products: [sailfin-gearless-24ft, sailfin-gearless-20ft, sailfin-geared-24ft, sailfin-geared-20ft]
recommended_controls: [smartair, smartair-multifan, touchair, wind-sensor]
source_docs:
  - "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt"
  - "Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt"
last_verified: 2026-04-11
---

# Dairy Barn Application

## Overview
Dairy barns are one of Envira-North's core HVLS applications. The goal is heat-stress mitigation for the herd: large fans moving a gentle, continuous air column over the stalls and feed alley to boost evaporative cooling and reduce standing heat and humidity. Dairy is classified as agricultural — wind sensor is mandatory.

## Recommended fans
- **Sailfin Gearless 20 ft or 24 ft** — the workhorses for dairy. Gearless means no gearbox oil change — lower long-term maintenance in a facility where operators are focused on the herd, not fan service.
- **Sailfin Geared 20 ft or 24 ft** — lower up-front cost, same cooling result, with the trade-off of a 20,000-hour gearbox oil change
- **24 ft** is the choice for wider free-stall barns; **20 ft** is better for narrower aisles

## Performance context (from Altra-Air D&E guide)
- HVLS fans create an **evaporative cooling effect of 3 to 4 degrees Celsius** throughout the facility during the cooling season
- During the heating season, the fan technology can **de-stratify uneven temperatures of up to 15°C from ceiling to floor**, reducing heating system cycling and delivering significant energy savings
- Operating cost: approximately **6 cents per hour** at 1 HP
- Greatly reduces "recovery" time when overhead doors are open with a constant air flow throughout

## Why HVLS for dairy
- Large, slow air column reaches the entire stall bed without creating drafts
- Lowers effective temperature at cow level during heat events
- Helps dry bedding and reduce ammonia accumulation
- Runs continuously through the day at modest power

## Recommended controls
- **SmartAIR or SmartAIR Multi-Fan** — **humidity automation is key** for dairy. Dairy is a high-humidity environment; temperature-only automation (TFD-1) misses a big part of the cow's heat-stress picture. SmartAIR can run the fans on the higher of temperature or humidity triggers.
- **TouchAIR** — for larger dairy operations with more than 10 fans, or when a BAS is integrated with the dairy management system
- **Wind Sensor** — **mandatory** for dairy (agricultural). Open-wall barns are exposed to side winds; the wind sensor decelerates the fan to a stop on gusts and restarts automatically.

## Design notes
- Spacing: 2.5× the fan diameter centre-to-centre for even coverage
- Minimum blade-to-floor clearance: 10 ft
- Mount the fans over the stall rows and the feed alley — not over the milking parlour if the parlour is a separate climate zone
- Verify the structural engineer has signed off on the dynamic load for the ceiling / truss

## Corrosion and hardware
- Dairy is a corrosive environment (ammonia, moisture, manure). Specify the appropriate blade and hardware finish when ordering — contact Envira-North Customer Support for the dairy-specific spec.
- Wipe-down / hose-down exposure: SmartAIR HMI should be mounted in the office or a dry control room, not in the barn proper. If the HMI must be in a wet area, use TouchAIR (NEMA4X).

## Wind sensor placement
- Mount the wind sensor outdoors in a representative location (not in a wind shadow, not on a leeward wall)
- Wire per `controls/wind-sensor.md`
- Test the trigger before each hot season

## Common pitfalls
- Skipping the wind sensor on an open-wall dairy → warranty concern, structural risk
- Using TFD-1 temperature-only automation → misses the humidity component of heat stress
- Mounting the HMI inside the wet barn area without NEMA4X → moisture damage
- Specifying 12 ft fans for a free-stall barn → undersized, poor coverage

## Common FAQs

**Q: What size fan for a 200-cow free-stall barn?**
A: 20 ft or 24 ft Sailfin, usually several of them spaced 2.5× diameter apart. Final count depends on barn length and roof height — contact Envira-North Customer Support for a layout.

**Q: Geared or gearless for dairy?**
A: Either works. Gearless is preferred for "install and forget" maintenance; geared is fine if the farm already services gearboxes.

**Q: Do I really need humidity automation?**
A: For dairy, yes — cow heat stress is as much a humidity problem as a temperature problem. That's why SmartAIR is recommended over LVC + TFD-1.

**Q: Is a wind sensor really required?**
A: Yes, for all agricultural installations. Dairy is agricultural. Skipping the sensor is a warranty and safety concern.

**Q: Can I mix Jazz fans in a dairy barn with my Sailfins?**
A: Jazz fans are indoor-only (IP54) and on their own network. They're not typically specified for agricultural barns. Consult Envira-North Customer Support.

## Source Documents Referenced
- `Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt`
- `Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt`
