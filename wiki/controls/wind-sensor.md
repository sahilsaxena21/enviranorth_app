---
id: wind-sensor
name: Wind Sensor
type: control
category: sensor
vfd: none
location: outdoor-mount
fans_controlled: multi
required_in: [agricultural]
works_with: [lvc, smartair, smartair-multifan]
source_docs:
  - "Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt"
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# Wind Sensor

## Overview
The Wind Sensor is a safety add-on that automatically decelerates a fan to a stop when measured outdoor wind speed exceeds a set point, and restarts the fan when wind drops back below the set point. It is **mandatory in all agricultural installations** of Envira-North HVLS fans. It works with SmartAIR / SmartAIR Multi-Fan (via the Schneider VFD path) and with the LVC (analogue path).

## Key Specifications
| Item | Value |
|---|---|
| Type | Outdoor wind-speed sensor |
| Trigger | Deceleration to stop when wind exceeds set point |
| Recovery | Automatic restart when wind drops below set point |
| Required in | All agricultural installations |
| Jumper requirement | If no sensor is installed, a jumper MUST be installed in its place for the fan to operate (SmartAIR-based installs) |
| Works with | SmartAIR, SmartAIR Multi-Fan, LVC, ZoneAIR, Schneider VFD standalone |

## Best Applications
- **All agricultural installations** — mandatory
- Any outdoor-exposed installation (open-wall barns, hay-storage buildings, riding arenas)
- Industrial facilities with large roll-up doors that expose fans to gusts

## Key Features & Benefits
- Automatic shutdown on high wind — protects the fan and the structure
- Automatic restart when wind drops — no operator intervention needed
- Alarm displayed on the SmartAIR HMI when triggered
- Works across both the Schneider VFD / SmartAIR path and the Lenze VFD / LVC path

## What Makes It Different
- **Safety-first, not a convenience feature.** Envira-North makes it mandatory for agricultural installs — the cost of skipping it is that the fan will not operate at all (a jumper must be installed in its place).
- **Automatic recovery** — unlike a fire relay, which may need a manual reset, the wind sensor restarts the fan on its own when wind drops.

## Power & Electrical Requirements
- Wired to the SmartAIR control box or the LVC (depending on the control path)
- Specific wiring diagrams are in the respective installation guides:
  - SmartAIR path: `Electrical Installation Guide - Schneider Drive`
  - LVC path: `Electrical Installation Guide 2022`
- If the wind sensor option was not ordered at time of manufacture, a factory-installed jumper occupies its wiring position. Removing the jumper without installing a real sensor will prevent the fan from running.

## Mounting & Installation Notes
- Mount outdoors in a location representative of real wind exposure (not sheltered, not in a wind-shadow)
- Specific mounting bracket and location details are in the installation guide — contact Envira-North for the recommended mounting procedure
- Route the sensor cable in its own conduit — do not run it with power cables
- Wire to the control as shown in the installation guide

## Maintenance Requirements
- Not separately documented in the wiki source text
- General guidance: inspect the sensor cup/vane for damage, debris, and smooth rotation at the same interval as fan maintenance (6 months initial, then every 18 months)
- Verify the trigger by simulating the high-wind condition before each season of heavy use (suggestion, not in source)

## Use with LVC and TFD-1
When the wind sensor is used alongside the LVC and TFD-1 temperature controller, the full system provides:
- Automatic fan start at a minimum temperature set point (TFD-1)
- Fan speed modulation across a temperature band (TFD-1)
- Automatic fan shutdown on high wind (Wind Sensor)
- Automatic fan restart when wind drops (Wind Sensor)

The Control Options brochure (2023) describes this combined function under the Wind Sensor entry: it works in conjunction with the LVC, uses a modulation-band to automate fan speed, and turns fans on at a minimum temperature set point. This combined description reflects the Wind Sensor + TFD-1 + LVC pairing.

## Compatible Accessories & Controls
- **SmartAIR / SmartAIR Multi-Fan** — triggers alarm display; auto-restart on wind drop
- **LVC / ZoneAIR** — triggers analogue shutdown; auto-restart
- **Schneider VFD standalone** — supported (per brochure)

## Common FAQs

**Q: Is a wind sensor required?**
A: Mandatory in all agricultural installations. Optional (but recommended) for any outdoor-exposed industrial or commercial install.

**Q: What happens if I skip the wind sensor on a SmartAIR install?**
A: A jumper must be installed in the sensor's place, or the fan will not operate. Do NOT leave the position empty.

**Q: What does the fan do when high wind is detected?**
A: It decelerates to a stop. The SmartAIR HMI displays an alarm message.

**Q: Does the fan restart automatically?**
A: Yes. When the measured wind speed drops below the set point, the fan restarts automatically — no operator action needed.

**Q: Is the wind sensor compatible with LVC?**
A: Yes. It integrates with the LVC on both Schneider and Lenze VFD networks.

**Q: Is the wind sensor the same as the fire relay?**
A: No. They are independent inputs. Fire relay triggers on fire-suppression-system activation; wind sensor triggers on measured wind speed. Each has its own jumper requirement if not installed.

**Q: Can I program the wind speed trigger?**
A: The set point is configurable — specific programming steps are in the installation guide. Contact Envira-North for the exact procedure.

**Q: What's the penalty for not installing a wind sensor in an agricultural install?**
A: The installation does not comply with the Envira-North installation requirements. It may also void the warranty. Always install the wind sensor in agricultural applications.

## Source Documents Referenced
- `Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt`
- `Electrical Installation Guide 2022 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
