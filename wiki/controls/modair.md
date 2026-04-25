---
id: modair
name: ModAIR (Lenze VFD + ModBus for SmartAIR/TouchAIR)
type: control
category: vfd-package
vfd: Lenze AC Tech
location: fan-mounted
fans_controlled: 1 per unit (needs additional ground HMI like SmartAIR or TouchAIR)
interface: requires external HMI
works_with: [sailfin-geared-8ft, sailfin-geared-12ft, sailfin-geared-16ft, sailfin-geared-20ft, sailfin-geared-24ft, sailfin-gearless-8ft, sailfin-gearless-12ft, sailfin-gearless-16ft, sailfin-gearless-20ft, sailfin-gearless-24ft, smartair, touchair]
source_docs:
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# ModAIR

## Overview
ModAIR is the Lenze-VFD-based path for digital HMI control. It is a fan-mounted package that includes the Lenze VFD, mounting plate, wiring harness, and a ModBus Communications Module. Because of the ModBus module, a ModAIR fan can be supervised by SmartAIR or TouchAIR — unlike ZoneAIR and EssentialAIR which are analogue. It requires a separate ground-level HMI; there is no standalone ModAIR interface.

## Key Specifications
| Item | Value |
|---|---|
| VFD make | Lenze AC Tech |
| Location | Fan-mounted |
| Communication | ModBus RTU |
| Fans per unit | 1 |
| Requires | External HMI (SmartAIR, TouchAIR) or BAS with ModBus |
| Optional internal fire relay | Available |
| Package includes | Lenze VFD, mounting plate, wiring harness, ModBus communications module |

## Best Applications
- Lenze-drive sites that want SmartAIR or TouchAIR digital HMI control
- Mixed installs where some fans use Schneider VFD + SmartAIR and others use Lenze + ModAIR, controlled from a single TouchAIR
- BAS-integrated sites that need ModBus RTU communication to the fans
- Commonly used with SmartAIR / TouchAIR or building automation systems (per the Control Options brochure)

## Key Features & Benefits
- Fan-mounted — short motor cable run
- Lenze VFD (same drive as ZoneAIR, CommandAIR, EssentialAIR)
- ModBus Communications Module included — enables digital HMI integration
- Can be controlled from the same TouchAIR as Schneider-VFD Sailfin fans
- Optional internal fire relay

## What Makes It Different
- **vs. ZoneAIR:** ZoneAIR is LVC (analogue, 0–10 V) control; ModAIR is ModBus (digital) control. ModAIR lets you use SmartAIR/TouchAIR touchscreen control; ZoneAIR does not.
- **vs. Schneider VFD:** both can talk to SmartAIR/TouchAIR. Schneider is a different drive family with NEMA4X enclosure and built-in CAT-5 connectivity. ModAIR is the Lenze-drive path to the same HMI ecosystem.
- **vs. EssentialAIR / CommandAIR:** neither has ModBus. ModAIR adds the ModBus module so a Lenze drive can talk to SmartAIR/TouchAIR/BAS.

## Power & Electrical Requirements
- Lenze AC Tech VFD — see `guides/electrical-install-lenze.md` for detailed FLC and cable-length rules
- Single-phase supported on 230 V (L1-L2 + PE); three-phase (L1-L2-L3 + PE)
- Separate insulated ground to each VFD from the panel
- Motor insulation class F
- No motor thermal wires — VFD handles overtemp/overload
- Min 1 ft (300 mm) VFD-to-fan separation
- ModBus communication wiring per SmartAIR or TouchAIR installation guide

## Mounting & Installation Notes
- Fan-mounted, mounting plate + wiring harness included
- Standard Lenze conduit rules apply (no input/output in same conduit, no control with power, etc.)
- Minimum programmed speed 15 Hz / 27 %
- Detailed SmartAIR/TouchAIR ModBus wiring is not in the extracted source text — contact Envira-North for the ModAIR + SmartAIR wiring diagram

## Maintenance Requirements
- VFD panel check at 12 months, then every 18 months
- Lock out the VFD and HMI during any fan/mount work
- See `guides/maintenance-schedule.md`

## Compatible Accessories & Controls
- **SmartAIR** — single-fan or multi-fan digital HMI
- **TouchAIR** — up to 20 fans, NEMA4X, BAS-ready
- **Fire relay** — optional internal Lenze VFD component
- **BAS via ModBus RTU** — ModAIR is the Lenze path for building automation

## Common FAQs

**Q: What's the difference between ModAIR and ZoneAIR?**
A: Both are fan-mounted Lenze VFD packages. ZoneAIR uses LVC (analogue 0–10 V, 7-wire daisy-chain) for control. ModAIR uses ModBus (digital) and works with SmartAIR, TouchAIR, and building automation systems. If you want a touchscreen or BAS integration on a Lenze drive, you need ModAIR.

**Q: Can ModAIR work without a separate HMI?**
A: No. ModAIR has no standalone interface — it needs SmartAIR, TouchAIR, or a BAS front end. For a self-contained Lenze package with its own keypad, see `controls/commandair.md` or `controls/essentialair.md`.

**Q: Can I run ModAIR and Schneider-VFD Sailfins on the same TouchAIR?**
A: Yes. TouchAIR supports Schneider VFDs, ModAIR, and Jazz fans (Jazz on its own network).

**Q: Does ModAIR include a fire relay?**
A: Optional internal fire relay.

**Q: What's the communication protocol?**
A: ModBus (referred to as ModBus or ModBus RTU in the source documents).

**Q: Can I upgrade an existing ZoneAIR to ModAIR?**
A: The Lenze VFD documentation says SmartAIR/TouchAIR can be used with ZoneAIR fans via ModBus communications "if the ZoneAIR unit is upgraded to ModAIR (ModBus module required)." Contact Envira-North to confirm the upgrade path for an existing install.

**Q: Does ModAIR support single-phase power?**
A: Yes, on the 230 V Lenze model.

## Source Documents Referenced
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
