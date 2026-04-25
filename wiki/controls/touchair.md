---
id: touchair
name: TouchAIR HMI
type: control
category: hmi
vfd: schneider
fans_controlled: up to 20
interface: touchscreen
enclosure: NEMA4X
works_with: [sailfin-geared-8ft, sailfin-geared-12ft, sailfin-geared-16ft, sailfin-geared-20ft, sailfin-geared-24ft, sailfin-gearless-8ft, sailfin-gearless-12ft, sailfin-gearless-16ft, sailfin-gearless-20ft, sailfin-gearless-24ft, aisle-air, jazz-fan, schneider-vfd, modair]
source_docs:
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2025-11"
version_source: "Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt"
supersedes: null
---

# TouchAIR HMI

## Overview
TouchAIR is Envira-North's top-end multi-fan touchscreen HMI. It controls up to 20 fans, comes in a NEMA4X enclosure, and is explicitly designed as a good fit for Building Automation Systems (BAS). It works with Schneider VFDs, ModAIR-equipped Lenze fans, and Jazz fans. The Control Options brochure (2023) states TouchAIR is "designed to work in conjunction with Schneider VFDs, ModAIR Fan Controls or Jazz Fans."

## Key Specifications
| Item | Value |
|---|---|
| Max fans | 20 |
| Interface | Touchscreen |
| Enclosure | NEMA4X |
| Power source | Not specified (likely separate supply — confirm with Envira-North) |
| Works with | Schneider VFD, ModAIR, Jazz Fans |
| BAS integration | Yes — designed for BAS |

## Best Applications
- Multi-fan facilities (up to 20 fans) needing single-point control
- BAS / BMS integrated installations
- Mixed-network sites (Schneider VFD Sailfins + ModAIR Lenze fans + Jazz fans — all manageable from one TouchAIR)
- Outdoor or washdown-prone environments (NEMA4X)

## Key Features & Benefits
- **Up to 20 fans from a single touchscreen** — the highest fan count of any Envira-North HMI
- **NEMA4X enclosure** — watertight, corrosion resistant
- **Designed for BAS integration** — Envira-North specifically positions TouchAIR as the BAS-friendly option
- Works with the three main fan drive/control paths: Schneider VFD, ModAIR (Lenze + ModBus), and Jazz fans
- Individual and group fan control

## What Makes It Different
- **vs. SmartAIR:** TouchAIR handles 2× the fans (20 vs. 10), is NEMA4X, and is BAS-ready. SmartAIR has built-in humidity sensing and LED light control — those features are not called out for TouchAIR in the source text.
- **vs. LVC:** LVC is analogue and caps at ~7–10 fans depending on drive. TouchAIR is digital, higher fan count, and BAS-integrable.
- **Mixed fleet support** — TouchAIR is the only HMI that can talk to all three fan paths (Schneider VFD, ModAIR Lenze, Jazz) in one installation, with Jazz on its own network.

## Power & Electrical Requirements
- NEMA4X enclosure — suitable for outdoor / washdown environments
- Specific wiring, voltage, current, and BAS protocol details are not captured in the OCR source text — contact Envira-North Customer Support for detailed specifications

## Mounting & Installation Notes
- Mount per standard HMI placement guidelines (dry, not exposed to direct sunlight, drafts, or exterior walls if temperature accuracy is important)
- NEMA4X means TouchAIR tolerates tougher mounting environments than SmartAIR
- Specific mounting steps are not in the OCR source text — contact Envira-North for the detailed installation procedure

## Maintenance Requirements
- Not documented separately. General guidance: VFD panel check at 12 months and every 18 months. Do not service while powered unless reprogramming or troubleshooting.

## Compatible Accessories & Controls
- **Schneider VFD** — primary partner for Sailfin fans
- **ModAIR** — Lenze VFD + ModBus, for Sailfin fans that are on the Lenze drive platform
- **Jazz Fans** — TouchAIR can supervise a Jazz network (Jazz runs on its own network, not mixed with Sailfin controls)
- **Wind Sensor / Fire relay** — available per the underlying VFD platform

## Jazz Fan HMI Reference (from Control Options Brochure 2023)
The following Jazz HMI information is included here for reference, as TouchAIR can supervise Jazz networks:

| Item | Jazz Fan HMI | Jazz Multi-Fan HMI |
|---|---|---|
| Included with | Purchase of Jazz Fan | Separate purchase |
| Fans controlled | 1 | Up to 5 |
| Communication cable | 100 ft CAT-5 (included) | CAT-5 daisy-chain between fans |
| Network topology | Single | Daisy-chain |

**Key notes:**
- Jazz fans must be on their **own separate network** — they cannot be mixed with Schneider VFD or Lenze VFD Sailfin fans on the same network
- The Jazz Multi-Fan HMI looks identical to the standard Jazz HMI but controls up to 5 fans
- TouchAIR is the only Envira-North HMI that can supervise a Jazz fan network alongside a Sailfin network

## Common FAQs

**Q: How many fans can TouchAIR control?**
A: Up to 20 fans.

**Q: What's the enclosure rating?**
A: NEMA4X — watertight and corrosion resistant.

**Q: Can TouchAIR talk to a building automation system?**
A: Yes. Envira-North positions TouchAIR as the "ideal component to use with BAS."

**Q: What fan drive platforms does TouchAIR work with?**
A: Schneider VFDs (for Sailfin), ModAIR (Lenze VFD + ModBus, for Sailfin), and Jazz Fans (on their own network).

**Q: Can TouchAIR control Jazz fans and Sailfin fans on the same project?**
A: Yes, but Jazz must be on its own network. TouchAIR supervises both networks from one HMI.

**Q: Does TouchAIR need a separate power source?**
A: Not explicitly documented in the Control Options brochure. Contact Envira-North to confirm.

**Q: Does TouchAIR do humidity-based automation like SmartAIR?**
A: Humidity sensing is not called out for TouchAIR in the source documents. It is a SmartAIR feature. Contact Envira-North to confirm whether TouchAIR has the same humidity feature.

**Q: What's the difference between TouchAIR and SmartAIR?**
A: See `comparisons/smartair-vs-touchair.md`. Short version: TouchAIR is bigger scale (20 fans vs. 10), NEMA4X, and BAS-ready. SmartAIR has humidity + LED light control and is more focused on smaller-scale single-zone automation.

**Q: Is there an Envira-North HMI that can control more than 20 fans?**
A: Not in the Control Options brochure. For larger fleets, contact Envira-North Customer Support about the LinkAir module (mentioned in some documents as a BACnet-based option supporting up to 247 fans with ZoneAIR).

## Source Documents Referenced
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `Envira-North 2025__Catalogue__EN__Rev-03__11.27.2025 (pdfplumber).txt`
