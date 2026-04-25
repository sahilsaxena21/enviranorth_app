---
id: application-warehouse
name: Warehouse / Distribution Centre Application
type: application
recommended_products: [sailfin-gearless-20ft, sailfin-gearless-24ft, sailfin-geared-20ft, sailfin-geared-24ft]
recommended_controls: [touchair, smartair-multifan, modair]
source_docs:
  - "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt"
  - "Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt"
last_verified: 2026-04-11
---

# Warehouse / Distribution Centre Application

## Overview
Warehouses and distribution centres are a strong fit for HVLS: large open floor plates, high ceilings, and workers plus forklifts covering long distances. The goal is worker comfort, air destratification (pulling warm ceiling air down in winter, cooling in summer), and keeping dock doors' cold air from pooling near pickers.

## Recommended fans
- **Sailfin Gearless 20 ft or 24 ft** — the workhorse. Gearless maintenance is a big win in a facility where a fan over a pick aisle is hard to reach with a lift.
- **Sailfin Geared 20 ft** — where budget leads and the operator has a lift plan for gearbox service
- **Sailfin Geared 16 ft** — for warehouses with lower ceilings where the 10 ft blade-to-floor clearance rules out a 20 ft fan (check ceiling height × 2 rule of thumb)

## Performance context (from Altra-Air D&E guide)
- HVLS fans create an **evaporative cooling effect of 3 to 4 degrees Celsius** throughout the facility during the cooling season
- During the heating season, the fan technology can **de-stratify uneven temperatures of up to 15°C from ceiling to floor**, reducing heating system cycling
- The 24 ft fan moves **315,026 CFM** (148,676 l/s) with a maximum effective coverage diameter of **230 ft (70 m)**
- Operating cost: approximately **6 cents per hour** at 1 HP
- Will minimize the need for expensive duct work in new construction for both heating and air conditioning systems
- A comfortable workplace environment **increases productivity and decreases absenteeism**

## Why HVLS for warehouses
- **Destratification (winter)** — warm air stuck at a 30 ft ceiling comes down to worker level. Reduces heating load.
- **Comfort cooling (summer)** — the air column creates an evaporative cooling effect of 3–4°C throughout the facility
- **One fan covers a large area** — a 24 ft fan moves 315,026 CFM, which would take many small ceiling fans to match
- **Low power draw per area covered** — 2 HP for a 24 ft fan; approximately 6 cents per hour at 1 HP

## Recommended controls
- **TouchAIR** — for 11–20 fans. Most mid-to-large distribution centres land in this fleet size. NEMA4X is useful near loading docks where the HMI might get splashed.
- **SmartAIR Multi-Fan** — for 2–10 fans, indoor mount. Cheaper than TouchAIR if the fleet is small and no BAS is needed.
- **ModAIR + TouchAIR** — if the warehouse is migrating from an older Lenze-drive installation, ModAIR bridges those drives into a TouchAIR HMI so the whole fleet is controlled from one screen
- **BAS / BMS integration** — use TouchAIR; it's the BAS-capable option

## Design notes
- Spacing: 2.5× diameter centre-to-centre
- Blade-to-floor: 10 ft minimum
- Fan layout: one fan per pick zone or racking block typically works; confirm with a design review
- Avoid placing fans directly over racking where air is blocked — put them over aisles or open staging areas
- **Dock doors:** fans help de-stratify but don't substitute for air curtains. A wind sensor is **not** usually required indoors, but consider one if the fan is near a large roll-up door that stays open

## Humidity
- Humidity automation is less critical in warehouses than in agricultural or food-processing facilities
- Temperature automation via SmartAIR is usually sufficient
- For pure-temperature automation at lower cost, LVC + TFD-1 + ZoneAIR is a valid alternative (Lenze VFD path)

## Common pitfalls
- Specifying a 24 ft fan in a building with less than 34 ft of ceiling (10 ft clearance + fan depth + service clearance)
- Mounting fans directly over high racking — air is blocked, fan underperforms
- Skipping the structural review on a truss-mounted install — the dynamic load is non-trivial
- Running fans below 15 Hz / 27 % to "save power" — motor overheats, warranty voided
- Ignoring BAS integration until late in the project — specify TouchAIR up front if BAS is planned

## Common FAQs

**Q: How many fans do I need for a 100,000 sq ft warehouse?**
A: Rough rule of thumb: 24 ft fans cover ~20,000 sq ft each, so 5 fans. Exact count depends on ceiling height, layout, and racking. Contact Envira-North Customer Support for a stocking layout.

**Q: Can the HVLS replace my HVAC?**
A: No — HVLS is an air-movement strategy, not a cooling or heating system. It makes existing HVAC more effective (reducing set-point on both sides) and creates perceived cooling from air movement.

**Q: Does it work in winter?**
A: Yes — this is destratification. Run the fans slowly in winter to mix the warm ceiling air down to worker level. SmartAIR / TouchAIR can automate reverse-season operation.

**Q: What HMI for a 15-fan distribution centre?**
A: TouchAIR — above 10 fans SmartAIR Multi-Fan maxes out.

**Q: Is a wind sensor required?**
A: Not for enclosed indoor warehouses. Required for agricultural, optional for outdoor-exposed fans.

## Source Documents Referenced
- `Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt`
- `Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt`
