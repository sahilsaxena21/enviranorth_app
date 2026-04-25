---
id: sailfin-geared-8ft
sku: EN675X5002
name: Altra-Air Sailfin Geared 8 FT
type: product
product_line: Altra-Air Sailfin Geared
size: 8 FT
size_metric: 2.4 M
drive: geared
categories: [hvls, ceiling-fan, industrial, agricultural, commercial]
applications: [small-workshop, small-barn, low-ceiling-industrial]
related: [sailfin-geared-12ft, sailfin-geared-16ft]
controls_compatible: [essentialair, zoneair, commandair, modair, schneider-vfd, smartair, lvc, touchair]
source_docs:
  - "Altra-Air 8FT Sailfin Spec Sheet 2022 (pdfplumber).txt"
  - "Altra-Air Sailfin Geared Brochure 2022 (pdfplumber).txt"
  - "Altra-AirSailfin-Custom (pdfplumber).txt"
  - "HogBrochure-Sailfin-EN (pdfplumber).txt"
  - "EN921X8240 Altra-AirSailfin_Geared&Gearless_InstallationGuide_11142024 (pdfplumber).txt"
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2024"
version_source: "EN921X8240 Altra-AirSailfin_Geared&Gearless_InstallationGuide_11142024 (pdfplumber).txt"
supersedes: null
---

# Altra-Air Sailfin Geared — 8 FT (EN675X5002)

## Overview
The Sailfin Geared 8 FT is the smallest Altra-Air Sailfin. A gearless 8 FT (EN670X5002) also exists in the lineup — see `products/sailfin-gearless-8ft.md` for the comparison. It uses a Nord helical in-line gearmotor and the same 5-blade Sailfin airfoil as the rest of the range. Intended for smaller industrial rooms, small barns, and any space where a 12 FT would be too large.

## Key Specifications
| Item | Value |
|---|---|
| SKU | EN675X5002 |
| Diameter | 2.4 m (8 ft) |
| Blade count | 5 (Sailfin airfoil, 6005 aluminum, anodized) |
| Drive | Nord helical in-line gearmotor |
| Maximum Velocity | 1.96 m/s (386 ft/min) |
| Airflow | 28,078 l/s (59,494 CFM) |
| Maximum Speed | 105 RPM |
| Power Usage | 782 W |
| Maximum Effective Diameter | 18 m (60 ft) |
| HP | 1 (50 Hz / 60 Hz) |
| Gear Ratio | 13.39 |
| Amps Consumed | 3 A @ 230 V |
| Torque | 53 Nm (39 ft-lbs) |
| Thrust | 125 N (28 lbs) |
| Insulation Class | F |
| Noise Level | 62.5 dBA |
| Weight (no mount) | 99 kg (220 lbs) |
| Voltage | 230 V / 400 V / 460 V / 575 V |
| Motor winding | 200°C ISR |
| LED light | Not included |
| Minimum ceiling height | 3.05 m (10 ft) |

## Best Applications
- Small workshops and equipment bays
- Small barns and livestock areas
- Low-ceiling industrial spaces where a larger fan won't fit within the 10 ft minimum clearance rule

## Key Features & Benefits
- Smallest Sailfin — fits spaces where 12+ ft HVLS fans are too large
- Helical in-line Nord gearmotor (robust, rated for continuous duty)
- 200°C ISR VFD-duty winding
- 5-blade Sailfin airfoil shared across the range with up to 23° angle of attack
- Blade top width of 10¼" on the airfoil for maximum airflow
- Produces an evaporative cooling effect of 3 to 4°C throughout the facility
- Lifetime warranty on blades and hub; 15-year prorated service life available (US/Canada) on registration within 30 days
- Whisper quiet operation; creates a non-disruptive airflow

## What Makes It Different
- There is no gearless 8 FT Sailfin — if you need a Sailfin at 8 ft diameter, this geared model is the only option.
- 1 HP motor (the smallest in the range); the 12 FT geared is also 1 HP, the 16 FT geared is 1.5 HP, and the 20 FT / 24 FT geared are 2 HP.
- Weighs 99 kg (220 lbs) — the lightest Sailfin.
- Like all geared Sailfins, it ships with a rubber vent plug in the gearbox that **must be removed and discarded before first start-up**.

## Power & Electrical Requirements
- One VFD per fan.
- Voltage options: 230 V / 400 V / 460 V / 575 V — the geared range supports 4 voltages vs. 230 V / 460 V on the gearless.
- VFD provides over-temperature and overload protection. Do not use motor thermal-protection wires.
- Separate insulated ground to each VFD from the panel.
- Motor insulation class F.
- Lenze VFD cable-length limits: 250 ft at 230 V, 160 ft at 460 V, 125 ft at 600 V (without add-on filters). Longer runs require a load reactor or dV/dT filter. See `guides/electrical-install-lenze.md`.

## Mounting & Installation Notes
- Minimum 10 ft (3.05 m) blade-to-floor clearance. Unguarded impeller — not for spaces accessible to people/animals.
- Mount types: OWSJ, Purlin Z, I-Beam, Wood Beam, Concrete Beam.
- Standard drops: 12", 24", 48"; custom available.
- 4-point 1/8" SS guy wire system, 45°–60° from frame, ~90° apart. No turnbuckles.
- Every connection requires its own safety cable.
- Min 1 ft (300 mm) VFD-to-fan separation.
- **Before first start-up:** remove the rubber vent plug from the gearbox and discard it. Discard the pink tag if attached. The yellow sticker (if present) can remain.

## Maintenance Requirements
- **Gearmotor oil:** check level at 18 months; change oil every 20,000 hours of normal operation. (This is the key maintenance difference vs. the gearless Sailfin.)
- Motor: hot-spot check + re-tighten electrical connections at 6 months, then every 18 months.
- Blades: inspect at 6 months, then every 18–36 months.
- Mounting/guys: physical check at 6 months, then every 18 months.
- VFD panel: at 12 months, then every 18 months.
- Schedule assumes ~5,000 hrs/year. Shorter intervals for humid or aggressive environments.
- Lock out controller during fan/mount work.

## Compatible Accessories & Controls
- **EssentialAIR** (wall-mount Lenze VFD) — simplest control — `controls/essentialair.md`
- **ZoneAIR** (fan-mounted Lenze VFD, needs LVC) — `controls/zoneair.md`
- **CommandAIR** (fan-mounted Lenze VFD + 100 ft remote keypad) — `controls/commandair.md`
- **ModAIR** (Lenze VFD + ModBus for SmartAIR/TouchAIR) — `controls/modair.md`
- **Schneider VFD** standalone — `controls/schneider-vfd.md`
- **SmartAIR / TouchAIR** (requires Schneider VFD or ModAIR) — `controls/smartair.md`, `controls/touchair.md`
- **LVC + TFD-1** — analogue daisy-chain control
- **Wind Sensor** — mandatory in agricultural installs
- **Fire relay** — optional internal component in all packages

## Common FAQs

**Q: Is there an 8 FT gearless Sailfin?**
A: Not in the source documents for this wiki. The 8 FT is only available as this geared model. Confirm with Envira-North Customer Support if a customer needs a gearless 8 FT.

**Q: Does the 8 FT geared Sailfin come with an LED light?**
A: No. LED is standard on gearless Sailfins only.

**Q: What do I need to do before turning the fan on for the first time?**
A: Remove the rubber vent plug from the gearbox and discard it. Missing this step is a known installation error on geared Sailfins.

**Q: How often do I change the gear oil?**
A: Check the oil level at 18 months. Full oil change every 20,000 hours of normal operation.

**Q: What voltages does the 8 FT geared support?**
A: 230 V, 400 V, 460 V, or 575 V. This is broader than the gearless range (230/460 only).

**Q: Can I use a Schneider VFD with the 8 FT geared?**
A: Yes. The Schneider VFD works with both the gearless and geared Sailfins. The Lenze-based packages (EssentialAIR, ZoneAIR, CommandAIR, ModAIR) are the other common choices.

**Q: What's the minimum ceiling height?**
A: 10 ft (3.05 m) from blade leading edge to floor. This applies to all Sailfin sizes, including the 8 FT.

## Warranty
| Component | Coverage |
|---|---|
| Motor, Gearbox & Control Panel | 3 Years |
| Blades, Hub & Mounting System | Lifetime |

*See Altra-Air Installation Guide for full warranty specifications and exclusions.*

## Agricultural / Hog Barn Applications
- HVLS fans provide constant mixing of air within the finishing room
- Inlets are counter-balanced and located directly above the large diameter fan
- Fresh air distribution by fans leads to a 30% reduction in exhaust capacity required
- More air speed reduces fly issues
- Fewer fans = lower operational cost and less maintenance
- Reverse capability enables winter circulation without drafts
- Less torque design reduces wear on drive train

## Designer Series — Custom Colours & Hydrographics
Custom blade colours are available for the Altra-Air Sailfin fans (note: the Custom brochure specifies 12' to 24' diameter; the 8 FT is not listed — verify with Envira-North if custom colours are required for the 8 FT). Options include:
- Custom painted or hydro-dipped blades in any colour, pattern, or design
- Matching hub label design included
- Corporate colour matching available to support brand consistency

## Source Documents Referenced
- `Altra-Air 8FT Sailfin Spec Sheet 2022 (pdfplumber).txt`
- `Altra-Air Sailfin Geared Brochure 2022 (pdfplumber).txt`
- `HogBrochure-Sailfin-EN (pdfplumber).txt`
- `Altra-AirSailfin-Custom (pdfplumber).txt`
- `EN921X8240 Altra-AirSailfin_Geared&Gearless_InstallationGuide_11142024 (pdfplumber).txt`
- `Electrical Installation Guide 2022 (pdfplumber).txt` — Sailfin fan electrical installation: EssentialAIR, ZoneAIR, CommandAIR (Lenze controls)
