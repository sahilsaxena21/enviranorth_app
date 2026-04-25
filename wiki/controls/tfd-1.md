---
id: tfd-1
name: TFD-1 Temperature Controller
type: control
category: sensor
vfd: none
location: wall-mount
fans_controlled: multi
requires: lvc
works_with: [alite-3, lvc, zoneair, schneider-vfd]
source_docs:
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# TFD-1 Temperature Controller

## Overview
The TFD-1 is an analogue temperature-controller add-on for the LVC. It uses a set point, modulation band, and minimum-ventilation-off temperature to automate fan speed based on measured temperature. It plugs into the LVC with 4 wires (18 AWG shielded). Unlike SmartAIR, the TFD-1 does not do humidity, and it does not use a touchscreen — it is a dial-based device.

## Key Specifications
| Item | Value |
|---|---|
| Requires | LVC (Low Voltage Control) |
| Connection to LVC | 4-wire 18 AWG shielded cable |
| Interface | Selector dial and adjustor dials |
| Automation | Temperature only (no humidity) |
| Minimum programmed fan speed | 15 Hz / 27 % (locked — do not lower) |
| Control signal | 0–10 V via the LVC |

## Best Applications
- Any LVC install that wants simple temperature-based automation without a touchscreen HMI
- Budget-conscious automation (adds minimal cost to LVC + ZoneAIR)
- Agricultural and industrial facilities where operators prefer physical dials over touchscreens

## Key Features & Benefits
- **Set point (position 1 on selector dial):** the temperature at which the fan begins to run
- **Modulation band (position 2):** the temperature range over which fan speed increases linearly from 27 % to 100 %
- **Minimum ventilation off (position 3):** the temperature below which the fan stops
- **Example:** set point 20 °C, modulation band 10 °C, min vent off 5 °C:
  - Fan starts at 20 °C
  - Speed ramps linearly from 27 % at 20 °C to 100 % at 30 °C
  - Fan runs at 100 % above 30 °C
  - Fan stops when temperature drops below 15 °C (set point minus min vent off)

## What Makes It Different
- **vs. SmartAIR auto mode:** SmartAIR is a digital touchscreen with both temperature AND humidity automation, plus LED control and real-time drive data. TFD-1 is temperature-only, dial-based, and no display. TFD-1 is simpler and cheaper; SmartAIR is more capable.
- **vs. manual LVC operation:** TFD-1 turns LVC into an automated controller. Without TFD-1, the LVC is manual (speed potentiometer set by the operator).

## Power & Electrical Requirements
- 4-wire 18 AWG shielded cable to the LVC
- Specific power supply details per `Electrical Installation Guide 2022`
- Minimum programmed fan speed: 15 Hz / 27 %. Do NOT lower — will overheat motor and void warranty.

## Mounting & Installation Notes
- Plugs into the LVC (physical panel mounting and wiring per the Electrical Installation Guide)
- "TFD-1 / Manual" toggle on the LVC switches between TFD-1-driven automation and manual potentiometer operation
- For manual operation, set the toggle to MANUAL

## Maintenance Requirements
- Not separately documented — follow the general LVC/VFD maintenance schedule
- Verify dial settings periodically — they do not drift, but ensure the set point still matches the facility's needs as seasons change

## Compatible Accessories & Controls
- **LVC** — required host
- **ZoneAIR (Lenze VFD)** — the most common pairing
- **Schneider VFD** — also supported via LVC
- **Wind Sensor** — integrates with LVC (independent of TFD-1)
- **Fire relay** — individual VFD option (independent of TFD-1)

## Common FAQs

**Q: What does TFD-1 do?**
A: It automates fan speed based on temperature. When temperature reaches the set point, the fan starts at 27 %. As temperature rises through the modulation band, speed ramps linearly to 100 %. When temperature drops, the process reverses; the fan stops below (set point – min vent off).

**Q: What's a practical example?**
A: Set point 20 °C, modulation band 10 °C, min vent off 5 °C → fan starts at 20 °C, full speed at 30 °C, stops at 15 °C.

**Q: Does TFD-1 control humidity?**
A: No — temperature only. For humidity-based automation, use SmartAIR.

**Q: Can I use TFD-1 without LVC?**
A: No. TFD-1 is an LVC add-on. It uses the LVC's 0–10 V output to the VFDs.

**Q: What's the minimum speed I can program?**
A: 15 Hz / 27 %. Locked. Do not lower — the motor overheats at lower speeds and the warranty is voided.

**Q: How do I switch between automatic (TFD-1) and manual control?**
A: Use the "TFD-1 / Manual" toggle on the LVC. Manual position uses the speed potentiometer; TFD-1 position uses the temperature controller.

**Q: Does TFD-1 work with Jazz fans?**
A: Jazz fans are on their own network and have their own HMI controls. TFD-1 is for Sailfin/Alite-style fans running through an LVC.

**Q: What's the difference between TFD-1 and SmartAIR's auto mode?**
A: TFD-1 is analogue, dial-based, temperature-only. SmartAIR is digital, touchscreen, temperature + humidity, plus LED and real-time data. Both use a set-point-plus-ramp concept, but SmartAIR is more capable and more expensive.

## Source Documents Referenced
- `Electrical Installation Guide 2022 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
