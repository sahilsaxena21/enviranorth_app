---
id: schneider-vfd
name: Schneider VFD (standalone)
type: control
category: vfd-package
enclosure: NEMA4X
location: fan-mounted
voltage_ranges: [200-240V, 380-500V, 525-600V]
input_phase: single-phase or three-phase
fans_controlled: 1 per unit
interface: built-in keypad
works_with: [sailfin-geared-8ft, sailfin-geared-12ft, sailfin-geared-16ft, sailfin-geared-20ft, sailfin-geared-24ft, sailfin-gearless-8ft, sailfin-gearless-12ft, sailfin-gearless-16ft, sailfin-gearless-20ft, sailfin-gearless-24ft, smartair, smartair-multifan, touchair, lvc]
source_docs:
  - "Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# Schneider VFD (standalone)

## Overview
The Schneider VFD is Envira-North's fan-mounted Variable Frequency Drive in a NEMA4X enclosure. It is used with the Altra-Air Sailfin (geared and gearless) and is the required drive for the SmartAIR and TouchAIR digital HMI control systems. The VFD can also be controlled via the LVC analogue network.

## Key Specifications
| Item | Value |
|---|---|
| Make | Schneider |
| Location | Fan-mounted |
| Enclosure | NEMA4X |
| Voltage ranges | 200–240 V, 380–500 V, or 525–600 V |
| Input phase | Single-phase (L1-L2 + PE) or three-phase (L1-L2-L3 + PE) |
| Single-phase from 3-phase supply | Use only two phases of the 3-phase supply |
| Compatible fan types | Standard Gearless or Gearmotor (Altra-Air Sailfin) fans |
| Recommended HP | 2 HP for all Altra-Air Sailfin sizes |
| Optional internal fire relay | Available |
| Included | Fan-mounted VFD, mounting plate + fasteners, 100 ft CAT-5 cable |
| LVC compatibility | Up to 10 Schneider VFDs on one LVC network (max 1000 ft) |

## Best Applications
- Any single-fan Sailfin install where NEMA4X and single-phase input matter
- All SmartAIR / SmartAIR Multi-Fan installs (Schneider VFD is required)
- All TouchAIR installs (requires Schneider VFD or ModAIR)
- Agricultural and washdown-prone environments (NEMA4X)

## Key Features & Benefits
- NEMA4X enclosure — watertight, corrosion-resistant
- Fan-mounted — short motor cable runs
- Accepts single-phase input (uses two phases of a three-phase supply)
- Optional internal fire relay (integrates with SmartAIR fire alarm display)
- Required drive for SmartAIR / TouchAIR touchscreen control
- Works with LVC (up to 10 units daisy-chained, max 1000 ft)

## What Makes It Different (vs. Lenze VFD)
- Schneider VFD is the path for the SmartAIR / TouchAIR touchscreen systems. Lenze VFD is used in EssentialAIR, ZoneAIR, CommandAIR, and ModAIR.
- Schneider is NEMA4X; Lenze enclosure rating is not specified in the source documents.
- Both accept single-phase input at 230 V.
- Schneider VFD-to-motor cable-length limits are not specified in the Schneider installation guide. For Lenze, detailed cable-length rules exist (see `guides/electrical-install-lenze.md`).

## Power & Electrical Requirements
- **Single-phase input:** L1 - L2 + PE (use two phases of a three-phase supply if only 3-phase is available)
- **Three-phase input:** L1 - L2 - L3 + PE
- **Motor output:**
  - 460 VAC: connect motor T1-T2-T3 per 460V wiring label
  - 230 VAC: connect motor T1-T2-T3 per 230V wiring label
- VFD provides over-temperature and overload protection — do not use motor thermal-protection wires
- Separate insulated ground must be run from the panel to each VFD
- Use adequately sized, shielded VFD-to-motor cable
- Continuous run between motor and VFD — no splices
- Motor insulation class F
- Min 1 ft (300 mm) VFD-to-fan separation

See `guides/electrical-install-schneider.md` for the full installation procedure.

## Mounting & Installation Notes
- Do not run input and output power cables in the same conduit
- Do not run control cables with any power cables in the same conduit
- Do not run different fans' output power cables in the same conduit
- CAT-5 (for SmartAIR / TouchAIR) connects to the RJ45 port **inside** the VFD enclosure — not the external one on the drive
- If the CAT-5 run exceeds 100 ft, use bulk CAT-5 with no couplers mid-run

## Maintenance Requirements
- No specific schedule in the Schneider installation guide
- Per the Altra-Air Installation Guide: VFD panel check at 12 months, then every 18 months — look for loose or discoloured wires, hot spots; re-tighten loose connections
- No maintenance on the controller while powered unless programming or troubleshooting
- Lock out the controller during any fan/mount/guy-wire maintenance

## Compatible Accessories & Controls
- **SmartAIR** / **SmartAIR Multi-Fan** — required digital HMI option
- **TouchAIR** — multi-fan touchscreen (up to 20 fans)
- **LVC + TFD-1** — analogue 0–10 V network control (up to 10 Schneider VFDs, 1000 ft)
- **Fire relay** — optional internal component
- **Wind Sensor** — integrates via SmartAIR; jumper mandatory if not installed

## Common FAQs

**Q: Does the Schneider VFD accept single-phase power?**
A: Yes. Use two phases of the three-phase supply (L1-L2 + PE). Three-phase is also accepted (L1-L2-L3 + PE).

**Q: What HP do I need for an Altra-Air Sailfin?**
A: Envira-North recommends a 2 HP Schneider VFD for all Altra-Air Sailfin sizes.

**Q: Where does the CAT-5 cable connect?**
A: To the RJ45 port **inside** the Schneider VFD enclosure — not the external RJ45 on the drive. This is a common mistake.

**Q: Can I use the Schneider VFD with the LVC?**
A: Yes. Up to 10 Schneider VFDs on one LVC network, max 1000 ft of cable.

**Q: Can I use the Schneider VFD with the Lenze-based control packages?**
A: No. EssentialAIR, ZoneAIR, CommandAIR, and ModAIR are Lenze-based. The Schneider VFD is a separate path.

**Q: Is the Schneider VFD NEMA4X?**
A: Yes. It is a fan-mounted NEMA4X drive.

**Q: What voltage options are there?**
A: Three ranges: 200–240 V, 380–500 V, and 525–600 V.

**Q: What comes in the box?**
A: The fan-mounted VFD, a mounting plate with fasteners, and a 100 ft CAT-5 cable.

## Source Documents Referenced
- `Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
