---
id: application-manufacturing
name: Manufacturing / Industrial Shop Floor Application
type: application
recommended_products: [sailfin-gearless-16ft, sailfin-gearless-20ft, sailfin-geared-16ft, sailfin-geared-20ft, aisle-air]
recommended_controls: [smartair-multifan, touchair, modair]
source_docs:
  - "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt"
  - "Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt"
last_verified: 2026-04-11
---

# Manufacturing / Industrial Shop Floor Application

## Overview
Manufacturing facilities are Envira-North's bread-and-butter industrial application. The goal is worker comfort and process-air management across a large shop floor with equipment, overhead crane rails, assembly lines, and loading docks. HVLS fans move air gently over a wide area without disrupting process-sensitive operations.

## Recommended fans
- **Sailfin Gearless 16 ft or 20 ft** — right-sized for most bays. 24 ft is overkill in a crowded shop with crane rails and columns; 16–20 ft threads through the obstructions more easily.
- **Sailfin Geared 16 ft or 20 ft** — same coverage, lower up-front cost
- **Aisle-Air** — for high-velocity directional airflow down specific aisles or lines. Different function from HVLS (high velocity, not high volume low speed) — pairs well with HVLS for targeted cooling at specific workstations.

## Performance context (from Altra-Air D&E guide)
- HVLS fans create an **evaporative cooling effect of 3 to 4 degrees Celsius** throughout the facility
- De-stratifies uneven temperatures of **up to 15°C from ceiling to floor**, reducing heating system cycling
- **Improves air quality** by lowering impurity levels caused by human respiration and toxic chemical emissions
- Lowers temperatures by cooling roof spaces and removing trapped ceiling heat through ceiling grilles
- A comfortable workplace environment **increases productivity and decreases absenteeism**
- Greatly reduces "recovery" time when overhead doors are open

## Why HVLS for manufacturing
- Worker comfort across large floor plates without zone-by-zone HVAC
- Helps exhaust systems by breaking up stagnant layers
- Winter destratification pulls warm process heat down to worker level
- Insensitive to the line layout — the air column drops straight down, so it works around obstructions

## Recommended controls
- **SmartAIR Multi-Fan** — for 2–10 fans in one shop zone, indoor
- **TouchAIR** — for larger multi-bay facilities (11–20 fans), or when the plant has a BMS that should command the fans
- **ModAIR + TouchAIR** — if retrofitting an older Lenze-drive installation into a single HMI
- **Individual EssentialAIR or CommandAIR** — for standalone single-fan installs at remote workstations

## Workstation-specific airflow
Some manufacturing operations need directional cooling at a specific workstation — welding bays, foundry lines, paint prep stations. HVLS alone gives the whole floor gentle airflow; it does not target a specific spot. For that, use:
- **Aisle-Air** — 15 MPH directional output, ducted or wall-mounted
- **Spot cooling fans** — not in the Envira-North catalogue; pair HVLS with third-party spot coolers as needed

## Process-air considerations
- **Welding:** HVLS shouldn't blow fume-extraction sideways out of capture hoods. Run the fans at lower speed in welding zones or shut them off during high-fume operations. SmartAIR can automate this with scheduling / zoning.
- **Painting / finishing:** don't use HVLS in a paint booth — it fights the booth's airflow pattern. HVLS is for the surrounding shop, not the booth interior.
- **Dust:** HVLS stirs fine dust. In dusty shops, coordinate with dust collection.
- **Cleanrooms:** not appropriate — HVLS defeats laminar flow.

## Electrical
- Most shops are on 460 V three-phase — both Schneider and Lenze drives support this natively
- Long motor cable runs on a Lenze drive may need a load reactor — see `guides/electrical-install-lenze.md`
- Schneider drives are NEMA4X out of the box — a plus in dusty / wet industrial environments

## Common pitfalls
- Running HVLS in a welding zone while capture hoods are on — diverts fume extraction
- Specifying 24 ft fans in bays with low crane rails — not enough clearance
- Skipping the structural review on a truss-mounted install
- Running below 15 Hz / 27 % "to stay quiet" — motor overheats, warranty voided

## Common FAQs

**Q: How do HVLS and Aisle-Air fit together?**
A: HVLS gives the whole floor gentle air movement; Aisle-Air gives specific aisles or stations high-velocity directional airflow. They're complementary, not competing.

**Q: Can I run HVLS over a paint booth?**
A: Not inside the booth. Outside the booth, yes — it helps the surrounding shop.

**Q: What's the right fan for a welding shop?**
A: 16 or 20 ft Sailfin running at low speed. Use SmartAIR to schedule or zone the fans so they don't disrupt fume extraction during peak welding.

**Q: 460 V three-phase — which VFD?**
A: Both Schneider and Lenze support 460 V. Choose the VFD based on the HMI you want, not the voltage.

**Q: Do I need a wind sensor?**
A: Only if fans are exposed to outdoor wind through a large open dock door. Not required for enclosed indoor shops.

## Source Documents Referenced
- `Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt`
- `Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt`
