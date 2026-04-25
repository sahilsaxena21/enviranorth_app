---
id: smartair-multifan
name: SmartAIR Multi-Fan
type: control
category: hmi
vfd: schneider
location: wall-mount
fans_controlled: up to 10
requires: schneider-vfd
works_with: [sailfin-gearless-8ft, sailfin-gearless-12ft, sailfin-gearless-16ft, sailfin-gearless-20ft, sailfin-gearless-24ft]
alias_of: smartair
source_docs:
  - "Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# SmartAIR Multi-Fan

> This is a variant of the SmartAIR HMI. All the SmartAIR content — auto mode, humidity integration, LED light control, wind sensor, fire relay, install rules — applies here. See **`controls/smartair.md`** for the full feature description. This page focuses specifically on the multi-fan differences.

## Quick summary
- Same SmartAIR touchscreen, same features (temperature + humidity auto mode, LED dimming, wind sensor and fire relay integration, real-time drive data)
- Scales from 1 fan (SmartAIR single-fan) to up to **10 fans** (SmartAIR Multi-Fan)
- Uses a **control box** with **RJ45 splitters** to create a star-then-daisy-chain topology from the HMI to the VFDs
- **Auto-mode settings are not retentive on power loss** (multi-fan only) — if the HMI loses power, auto mode resets to Disabled and must be re-enabled manually

## Included Components (from Schneider Electrical Installation Guide)
- HMI Control (SmartAIR touchscreen)
- Control Box
- RJ45 Splitters
- 100 ft CAT-5 Cable

## Network setup (from the Schneider Electrical Installation Guide)

1. Connect the supplied RJ45 splitter to the short CAT-5 cable inside VFD 1
2. Connect the CAT-5 cable from the control box to one port of the splitter
3. Connect a CAT-5 cable from VFD 1 to VFD 2 on the other splitter port
4. Continue in the same manner for each subsequent VFD
5. The last VFD in the network does **not** need a splitter — connect the CAT-5 from the previous VFD directly to its internal RJ45 port
6. All CAT-5 connections must be made inside an enclosure
7. Inside the control box, connect the HMI CAT-5 and the VFD #1 CAT-5 to the labelled connectors, then connect the power supply to the receiver on the bottom of the control box

## Control box placement
- Mount in a dry location
- Do not wash with pressurised water
- Provisioned for wind sensor and fire relay. If either was not ordered at time of manufacture, a factory-installed jumper occupies its position — leave the jumper in place or the fan will not operate

## Differences from the single-fan SmartAIR
- **Retention on power loss:** single-fan HMI behaviour is not specified in source; multi-fan auto mode explicitly resets to Disabled when power is lost
- **Physical topology:** single-fan is a direct HMI-to-VFD CAT-5 run; multi-fan uses a control box with RJ45 splitters daisy-chaining VFDs
- **Max fans:** 1 vs. 10
- **Control box:** only on multi-fan — single-fan uses the VFD directly

## Common FAQs specific to multi-fan

**Q: How many fans can SmartAIR Multi-Fan control?**
A: Up to 10 fans on one HMI.

**Q: What happens if I lose power to the HMI?**
A: Auto-mode settings reset to Disabled. You must re-enable them after power restoration for the fans to run in auto mode again. This is documented specifically for the multi-fan HMI.

**Q: What topology does the multi-fan version use?**
A: Star from the control box to VFD #1, then daisy-chain VFD-to-VFD using RJ45 splitters inside each VFD enclosure. The last VFD in the chain does not use a splitter.

**Q: Where do the CAT-5 connections go?**
A: All connections must be made **inside** an enclosure (either the VFD enclosure or the control box). Never use the external RJ45 on the drive.

**Q: What happens if one VFD in the daisy-chain loses power?**
A: The Control Options and Schneider installation guide imply that all VFDs must be powered for the system to operate (similar to the ZoneAIR LVC rule). Contact Envira-North Customer Support for specific multi-fan failover behaviour.

**Q: Can I expand from 10 fans to more?**
A: Not on SmartAIR Multi-Fan. For 11+ fans, use TouchAIR (up to 20 fans, NEMA4X, BAS-capable).

See `controls/smartair.md` for all other questions (auto mode, humidity, LED, wind sensor, fire relay, mounting).

## Source Documents Referenced
- `Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
