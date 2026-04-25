---
id: lvc
name: LVC (Low Voltage Control)
type: control
category: zone-controller
vfd: none
location: wall-mount
fans_controlled: multi
signal: 0-10 V
max_fans: 7 (ZoneAIR) / 10 (Schneider VFD)
max_cable_length: 700 ft (ZoneAIR) / 1000 ft (Schneider VFD)
works_with: [sailfin-geared-8ft, sailfin-geared-12ft, sailfin-geared-16ft, sailfin-geared-20ft, sailfin-geared-24ft, sailfin-gearless-8ft, sailfin-gearless-12ft, sailfin-gearless-16ft, sailfin-gearless-20ft, sailfin-gearless-24ft, alite-3, aisle-air, zoneair, schneider-vfd]
source_docs:
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
  - "Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# LVC (Low Voltage Control)

## Overview
The LVC is Envira-North's analogue ground-level multi-fan controller. It uses a 0–10 V signal daisy-chained from VFD to VFD and provides manual speed, forward/reverse, and emergency stop for a group of fans. Unlike SmartAIR/TouchAIR, it is not a touchscreen — it is a physical panel with a speed potentiometer, stop button, toggles, and an optional TFD-1 temperature-controller dial. Works with both Lenze (ZoneAIR) and Schneider VFDs.

## Key Specifications
| Item | ZoneAIR (Lenze) | Schneider VFD |
|---|---|---|
| Max fans on network | 7 | 10 |
| Max total cable length | 700 ft (214 m) | 1000 ft (305 m) |
| Cable | 7-wire 18 AWG shielded | 6-wire shielded, 18 AWG min |
| Signal | 0–10 V | 0–10 V |
| Topology | Daisy-chain VFD to VFD | Daisy-chain VFD to VFD |

## Best Applications
- Multi-fan zones needing a simple, cost-effective manual controller
- Facilities that want a physical stop button and speed dial instead of a touchscreen
- Temperature-based automated control paired with the TFD-1
- Mixed installs using both Schneider and Lenze VFDs (LVC works with both)
- Wind-sensor integration in agricultural installs

## Key Features & Benefits
- **Manual control panel:**
  - Speed potentiometer
  - Forward/reverse toggle (can be used while fan is in motion)
  - Red stop button (used to stop the fan safely)
  - TFD-1 / Manual toggle (switches between auto temperature control and manual)
- **Compatible with both VFD families** — Lenze (ZoneAIR) and Schneider
- **Daisy-chain topology** — simple to wire up for multiple fans
- **TFD-1 integration** — adds temperature-based automation
- **Wind Sensor integration** — automatic fan stop on high wind
- **Emergency stop** via the red button on the LVC panel

## What Makes It Different
- **vs. SmartAIR/TouchAIR:** LVC is analogue, dial-based, no touchscreen, no humidity sensing, no LED light control, no real-time drive data. SmartAIR/TouchAIR are all of those.
- **vs. CommandAIR / EssentialAIR:** LVC controls multiple fans together. CommandAIR and EssentialAIR are single-fan.
- **vs. on-drive keypads:** LVC is a ground-level panel; no climbing required.

## Power & Electrical Requirements

### ZoneAIR / Lenze LVC wiring
- 7-wire 18 AWG shielded cable between LVC and the VFDs
- Terminal 6 is not connected between the 1st and 2nd VFD, nor between the 2nd and 3rd VFD
- Max cable distance from LVC to last VFD: 700 ft (214 m)
- All VFDs in the network must have individual power on for any fan to operate
- Emergency stop connects to the LVC
- TFD-1 connects to the LVC via 4 wires (18 AWG shielded)

### Schneider VFD LVC wiring
- All 6 control wires daisy-chained from the 1st VFD to the 2nd, and onward
- Repeat for every VFD on the network
- Max 10 Schneider VFDs per LVC network
- Shielded cable, 18 AWG minimum
- Max total cable length: 1000 ft (305 m)

## Mounting & Installation Notes
- **Never stop a running fan with a disconnect switch** — always use the red stop button on the LVC
- For manual operation, set the TFD-1/Manual toggle to MANUAL
- Adjust speed with the speed potentiometer
- Use the forward/reverse toggle to reverse direction while the fan is in motion
- Minimum fan speed is 15 Hz / 27 % — do not program the LVC or TFD-1 to go below this (will overheat motor, void warranty)

## Maintenance Requirements
- See `guides/maintenance-schedule.md` — VFD panel check at 12 months, then every 18 months
- Lock out the LVC and each individual VFD during fan/mount work
- Periodic inspection of the LVC panel itself — no specific interval given in source

## Compatible Accessories & Controls
- **TFD-1 Temperature Controller** — adds temperature-based automation
- **Wind Sensor** — automatic stop on high wind, auto restart when wind drops
- **Fire relay** — individual VFD option
- **Schneider VFD** — up to 10 per LVC network
- **Lenze VFD (ZoneAIR)** — up to 7 per LVC network

## Common FAQs

**Q: What's the difference between LVC + ZoneAIR and LVC + Schneider VFD in terms of fan count and cable length?**
A: ZoneAIR (Lenze): up to 7 fans, max 700 ft total. Schneider: up to 10 fans, max 1000 ft total.

**Q: How many wires does the LVC cable have?**
A: 7 wires on the ZoneAIR/Lenze side (18 AWG shielded). 6 wires on the Schneider side (18 AWG min, shielded).

**Q: Can I mix Schneider and Lenze VFDs on one LVC?**
A: The Control Options brochure says the LVC "can be used with Lenze & Schneider VFD's" but does not specify mixed networks. Treat as a same-family network and contact Envira-North Customer Support to confirm mixed-family configurations.

**Q: How do I stop a fan safely with LVC?**
A: Use the red stop button. Never stop a running fan with a disconnect switch.

**Q: Is the LVC a touchscreen?**
A: No. It's an analogue panel with a potentiometer, toggle switches, and a red stop button.

**Q: Can LVC automate based on temperature?**
A: Yes — with the optional TFD-1 temperature controller, which plugs into the LVC. Set point + modulation band + minimum-ventilation-off temperature.

**Q: Can LVC automate based on humidity?**
A: No. Humidity-based automation is a SmartAIR-only feature.

**Q: What's the maximum fan count per LVC network?**
A: 7 fans on ZoneAIR (Lenze), 10 fans on Schneider VFD.

**Q: Does the LVC need a separate power supply?**
A: Yes — the ZoneAIR (Lenze) LVC is powered by **240 VAC, 1PH** per the Electrical Installation Guide 2022 wiring diagram. Refer to the specific installation guide for full wiring details.

## Source Documents Referenced
- `Electrical Installation Guide 2022 (pdfplumber).txt`
- `Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
