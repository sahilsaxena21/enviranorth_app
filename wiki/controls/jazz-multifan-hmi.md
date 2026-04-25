---
id: jazz-multifan-hmi
name: Jazz Multi-Fan HMI
type: control
category: hmi
vfd: none
location: wall-mount
fans_controlled: up to 5
works_with: [jazz-fan]
source_docs:
  - "EN561X8455 Jazz_Installation Guide_EN__Rev-03__05.29.2025 (pdfplumber).txt"
  - "JazzDesign&EngineeringGuide-Updated10.18.2024 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2025-05"
version_source: "EN561X8455 Jazz_Installation Guide_EN__Rev-03__05.29.2025 (pdfplumber).txt"
supersedes: null
---

# Jazz Multi-Fan HMI

## Overview
The Jazz Multi-Fan HMI is the multi-fan version of the standard Jazz Fan HMI. It looks identical to the single-fan HMI but controls up to 5 Jazz Fans daisy-chained together with CAT-5 cable. Jazz fans remain on their own dedicated network — the Jazz Multi-Fan HMI cannot control non-Jazz fans.

## Key Specifications
| Item | Value |
|---|---|
| Max fans | 5 |
| Communication | CAT-5 daisy-chain, Jazz control protocol |
| Appearance | Identical to single-fan Jazz HMI |
| Features | Same as single-fan HMI (start/stop, speed, LED on/off, dimming) |
| Indoor use | Yes (IP54 / NEMA 3 — Jazz Fan system rating) |

## Best Applications
- 2–5 Jazz Fans in one space (restaurants with multiple zones, multi-aisle gymnasiums, amusement parks with several fans)
- Any install where one operator should be able to control a small group of Jazz fans from a single location

## Key Features & Benefits
- Same touch/HMI experience as the single-fan Jazz HMI
- CAT-5 daisy-chain — simple to wire between Jazz fans
- Up to 5 fans on one HMI
- Dims and switches the integrated Jazz LED on each fan
- Automatic thermal limiting on each fan (handled by the Jazz drive, not the HMI)

## What Makes It Different
- **vs. single-fan Jazz HMI:** same UI and form factor, but controls up to 5 fans via daisy-chain instead of just 1.
- **vs. SmartAIR Multi-Fan:** SmartAIR Multi-Fan is for Altra-Air Sailfin fans (up to 10 fans) on Schneider VFDs. Jazz Multi-Fan HMI is Jazz-only, max 5 fans, and uses Jazz's on-board drive — no separate VFD per fan.
- **vs. TouchAIR:** TouchAIR can supervise a larger Jazz zone (up to 20 fans combined across Schneider/ModAIR/Jazz networks, with Jazz on its own network). Jazz Multi-Fan HMI is the dedicated Jazz-only option for smaller fleets.

## Power & Electrical Requirements
- Pulls power from the Jazz fan network — no separate power supply
- Max permissible control cable length: 30 metres unshielded per the Jazz installation guide
- Wiring per the Jazz installation guide's MULTI-FAN CONTROL section

## Advanced Control Integration (SmartAIR / TouchAIR)
When integrating Jazz fans with Modbus-based SmartAIR or TouchAIR controllers, the Jazz Multi-Fan HMI remains in the Jazz fan network. The table below is from the Jazz installation guide:

| Controller | Number of fans | Max cable length | Power supply |
|---|---|---|---|
| SmartAIR (Single Fan) | 1 | 100 ft | VFD |
| SmartAIR Multi-Fan | 10 | 1,000 ft | External |
| TouchAIR | 20 | 4,000 ft | Internal power supply |

- Jazz fans must be on their own network separate from Schneider VFD / ModAIR fans.
- If cable lengths between devices exceed 100 ft (30 m), bulk cable must be used to create uninterrupted cables. Only couplers or splitters are permitted at each device (no intermediate junctions).
- Local electromagnetic interference may reduce effective cable lengths and may require shielded cable or signal repeaters.

## Mounting & Installation Notes
- Mount in a safe, dry indoor location
- Daisy-chain CAT-5 between Jazz fans per the installation guide
- Do not mix Jazz fans with Sailfin / ZoneAIR / SmartAIR networks

## Maintenance Requirements
- Thermal limiting is automatic on each Jazz fan
- No routine HMI maintenance documented
- Lock out each Jazz fan before any physical maintenance
- Wait 5 minutes after disconnecting power before working on the drive (Jazz capacitors take 5 minutes to discharge)

## Compatible Accessories & Controls
- **Jazz Fans** (up to 5)
- **TouchAIR** — can supervise a Jazz zone as a separate network

## Common FAQs

**Q: How many Jazz fans can the Jazz Multi-Fan HMI control?**
A: Up to 5 Jazz fans, daisy-chained with CAT-5.

**Q: Does the Jazz Multi-Fan HMI look different from the single-fan version?**
A: No — the two look identical. The difference is in configuration/firmware, not the physical HMI.

**Q: Can I control 6 or more Jazz fans from a single HMI?**
A: Not with the Jazz Multi-Fan HMI — its limit is 5. For larger Jazz fleets, TouchAIR can supervise the Jazz network as a separate zone.

**Q: Can I add a Sailfin fan to a Jazz Multi-Fan HMI network?**
A: No. Jazz fans must be on their own network.

**Q: Does the Jazz Multi-Fan HMI need a separate power supply?**
A: No — it pulls power from the Jazz fan network.

**Q: Is the Jazz Multi-Fan HMI outdoor rated?**
A: No. The Jazz Fan system is IP54 / NEMA 3 and for indoor use only.

## Source Documents Referenced
- `EN561X8455 Jazz_Installation Guide_EN__Rev-03__05.29.2025 (pdfplumber).txt`
- `JazzDesign&EngineeringGuide-Updated10.18.2024 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
