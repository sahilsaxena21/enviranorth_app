---
id: application-arena-gym
name: Arena / Gymnasium / Riding Arena Application
type: application
recommended_products: [sailfin-gearless-24ft, sailfin-gearless-20ft, sailfin-geared-24ft, jazz-fan]
recommended_controls: [smartair-multifan, touchair, jazz-multifan-hmi, wind-sensor]
source_docs:
  - "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "EN561X8455 Jazz_Installation Guide_EN__Rev-03__05.29.2025 (pdfplumber).txt"
  - "Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt"
  - "Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt"
last_verified: 2026-04-11
---

# Arena / Gymnasium / Riding Arena Application

## Overview
Large-volume public spaces — sports arenas, gymnasiums, horse riding arenas, event halls. The goal is comfort for occupants (players, spectators, horses) across a large floor plate with a high ceiling. HVLS is a strong fit because the air column covers a wide area with one low-noise fan.

## Recommended fans

### Sailfin Gearless 20 ft / 24 ft
- **First choice for large arenas** (hockey rinks, basketball court complexes, equestrian arenas)
- 24 ft at 315,000 CFM covers the typical rink / court footprint with one fan per bay
- Gearless = near-silent operation at low speeds, important in quiet spectator spaces

### Sailfin Geared 20 ft / 24 ft
- Same coverage, lower up-front cost, at the trade-off of the gearbox service interval

### Jazz Fan
- For **smaller / multi-zone spaces** (smaller studios, gym break rooms, equestrian offices)
- Indoor-only (IP54), 7–10 ft, integrated LED, Modbus
- Pairs well with Sailfin in the main arena + Jazz in auxiliary spaces

## Recommended controls
- **SmartAIR Multi-Fan** — 2–10 Sailfin fans in one arena. Humidity automation is a bonus for ice arenas (controls condensation) and riding arenas (dust suppression indirect — humidity tracking).
- **TouchAIR** — 11–20 fans, or a multi-space venue with a BAS
- **Jazz Multi-Fan HMI** — up to 5 Jazz fans in auxiliary spaces, Jazz-only network
- **Wind Sensor** — **mandatory for riding arenas** (classified as agricultural in most jurisdictions)

## Performance context (from Altra-Air D&E guide)
- HVLS fans create an **evaporative cooling effect of 3 to 4 degrees Celsius** throughout the facility
- De-stratifies uneven temperatures of **up to 15°C from ceiling to floor**, reducing heating system cycling
- The 24 ft Sailfin covers a maximum effective diameter of **230 ft (70 m)**
- The 20 ft Sailfin covers a maximum effective diameter of **200 ft (61 m)**
- **Aerodynamic blade noise is less than 1/5 of conventional fans** — important for spectator venues

## Why HVLS for arenas
- **Large, quiet air column** — the blades spin slowly so there's no whine; noise level as low as 45 dBA (gearless)
- **Even coverage** — one or two fans cover an entire court / rink
- **Dust control in riding arenas** — gentle air movement keeps dust from hanging in the air column at horse-nose height
- **Condensation management in ice rinks** — air circulation reduces ceiling condensation and "rain" over the ice

## Ice rink specifics
- Humidity automation via SmartAIR is especially valuable — ceiling condensation is a humidity problem
- Blade-to-floor (ice) clearance: 10 ft minimum, typically much more in an arena
- Confirm the ice-plant contractor's airflow expectations before specifying fan count

## Riding arena specifics
- **Classified as agricultural** — wind sensor is mandatory
- Open-wall riding arenas are exposed to side winds — position the wind sensor appropriately
- Dust is a health concern — verify air movement is gentle enough not to stir the footing
- 20 ft or 24 ft Sailfin fans work well over standard riding arena footprints

## Gymnasium specifics
- Indoor, enclosed, no wind sensor needed
- SmartAIR Multi-Fan (up to 10) is usually sufficient
- Schedule integration: use TouchAIR + BAS if the gym is part of a school / facility with central BMS

## Design notes
- Blade-to-floor: 10 ft minimum (more in spectator venues where trussing is high)
- Fan spacing: 2.5× diameter centre-to-centre
- Mount above the playing surface or ice, not over seating — the air column drops straight down

## Common pitfalls
- Skipping wind sensor on an open-wall riding arena
- Specifying 24 ft fans in a low-ceiling gym — check the clearance math
- Mounting fans directly over seating — occupants feel cold draft
- Running ice-rink fans at too high a speed in winter — over-cooling already-cold air

## Common FAQs

**Q: Will the fans scare the horses?**
A: HVLS blades spin slowly (50–100 RPM) and are quiet. Most horses acclimate within a few sessions. Ramp speed gradually during introduction.

**Q: Ice rink — doesn't circulation melt the ice faster?**
A: No. HVLS at low speed improves the heat balance by reducing ceiling condensation and distributing the cold air column more evenly. The ice plant doesn't have to fight warm pockets. Ice-plant contractors generally endorse HVLS for this reason.

**Q: Can I use Jazz fans in the main arena?**
A: Jazz is 7–10 ft — too small for a full arena. Use Sailfin 20/24 ft in the main space and Jazz in lobbies / offices / locker rooms.

**Q: SmartAIR vs. TouchAIR for a 4-rink complex?**
A: TouchAIR — a 4-rink complex usually has more than 10 fans total, and TouchAIR can supervise the whole complex on one screen.

**Q: Is a wind sensor required for an indoor gym?**
A: No. Enclosed indoor spaces don't need the wind sensor. It's required for agricultural and recommended for outdoor-exposed installs.

## Source Documents Referenced
- `Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `EN561X8455 Jazz_Installation Guide_EN__Rev-03__05.29.2025 (pdfplumber).txt`
- `Altra-AirSailfin_Design&Engineering_2022 (pdfplumber).txt`
- `Altra-AirSailfinGearless_Design&Engineering_202215YearWarranty (pdfplumber).txt`
