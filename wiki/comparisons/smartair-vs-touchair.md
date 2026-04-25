---
id: smartair-vs-touchair
name: SmartAIR vs. TouchAIR
type: comparison
compares: [smartair, smartair-multifan, touchair]
source_docs:
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt"
last_verified: 2026-04-11
---

# SmartAIR vs. TouchAIR

## TL;DR
- **SmartAIR** — touchscreen HMI for 1–10 fans, indoor, Schneider VFD path. Temp + humidity auto mode, LED dimming, wind sensor, fire relay.
- **TouchAIR** — larger-zone HMI for up to 20 fans, **NEMA4X outdoor-rated**, **BAS-capable**, can supervise Schneider + ModAIR + Jazz networks.

## When to choose SmartAIR
- 1–10 Sailfin fans on Schneider VFDs
- Indoor, dry mounting location
- Don't need BAS / BMS integration
- Want the simpler (and cheaper) of the two touchscreen options

## When to choose TouchAIR
- 11–20 fans in one zone
- Outdoor or wet mounting location (NEMA4X)
- Facility has a BAS / BMS that needs to talk to the fan zone
- Mixed fleet: Sailfin on Schneider + Sailfin on Lenze (ModAIR) + Jazz fans in the same supervised area

## Side-by-side
| Item | SmartAIR | SmartAIR Multi-Fan | TouchAIR |
|---|---|---|---|
| Max fans | 1 | 10 | 20 |
| Enclosure | Indoor | Indoor (control box) | **NEMA4X outdoor** |
| BAS / BMS | No | No | **Yes** |
| Temperature auto | Yes | Yes | Yes |
| Humidity auto | Yes | Yes | Yes |
| LED dimming | Yes | Yes | Yes |
| Wind sensor | Yes | Yes | Yes |
| Fire relay | Yes | Yes | Yes |
| Schneider VFD | Yes | Yes | Yes |
| Lenze VFD (via ModAIR) | No | No | **Yes** |
| Jazz (as a supervised zone) | No | No | **Yes** |
| Auto-mode retentive on power loss | Not specified | **No** (resets to Disabled) | Not specified |
| Topology | Direct HMI-to-VFD CAT-5 | Control box + RJ45 splitters daisy-chain | Networked across zones |

> **Note:** The TouchAIR humidity auto-mode and LED dimming entries in the table above are not explicitly confirmed in the Control Options brochure (2023) source text for TouchAIR specifically. These features are confirmed for SmartAIR. Confirm TouchAIR humidity/LED capability with Envira-North before specifying.

## Key architectural differences
- **SmartAIR** is the "single-network" HMI — it only talks to Schneider VFDs. The multi-fan version adds a control box and a star-then-daisy-chain topology but stays within one network.
- **TouchAIR** is the "supervisor" HMI — it can see multiple networks simultaneously (Schneider, ModAIR bridging to Lenze, Jazz on its own network).
- NEMA4X on TouchAIR means it can be mounted in wash-down areas, loading docks, or outdoor shelters. SmartAIR cannot.

## Cost consideration (qualitative)
- SmartAIR is the lower-cost touchscreen option
- TouchAIR costs more but is required above 10 fans or when BAS is needed
- The break-even is around 10 fans — at 10 fans exactly, SmartAIR Multi-Fan will usually win on cost if no BAS is needed and the mount is indoor

## Jazz Fan Network Notes (from Control Options Brochure 2023)
- Jazz fans use their own HMI (Jazz Fan HMI or Jazz Multi-Fan HMI) — these are entirely separate from the SmartAIR and TouchAIR ecosystems
- **SmartAIR cannot supervise Jazz fans.** Jazz fans must be on their own network.
- **TouchAIR can supervise a Jazz network** alongside Sailfin networks — it is the only Envira-North HMI with this capability
- Jazz Fan HMI: controls 1 Jazz fan, includes 100 ft CAT-5 cable, included with Jazz Fan purchase
- Jazz Multi-Fan HMI: controls up to 5 Jazz fans, daisy-chain connected with CAT-5

## Common FAQs

**Q: I have 8 fans indoors and no BAS. Which HMI?**
A: SmartAIR Multi-Fan — cheaper, same features minus BAS.

**Q: I have 12 fans. Which HMI?**
A: TouchAIR — SmartAIR Multi-Fan maxes at 10.

**Q: I have 6 Sailfin fans indoor plus 4 Jazz fans. Which HMI?**
A: TouchAIR — it's the only option that can supervise Jazz as a separate zone alongside Sailfin.

**Q: Does SmartAIR keep auto mode after a power loss?**
A: Single-fan: not specified in the source. Multi-fan: **no** — auto mode resets to Disabled and must be re-enabled by the operator.

**Q: Is TouchAIR always a better choice than SmartAIR?**
A: No — for small indoor fleets with no BAS, SmartAIR is cheaper and simpler. TouchAIR's capacity and NEMA4X don't add value there.

## Source Documents Referenced
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt`
