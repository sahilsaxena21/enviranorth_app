---
id: zoneair
name: ZoneAIR (fan-mounted Lenze VFD for LVC zone control)
type: control
category: vfd-package
vfd: Lenze AC Tech
location: fan-mounted
fans_controlled: 1 per unit (needs additional ground control like LVC)
interface: needs external controller
works_with: [sailfin-geared, sailfin-gearless, lvc, tfd-1]
source_docs:
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# ZoneAIR

## Overview
ZoneAIR is a fan-mounted Lenze VFD package built for multi-fan zone control via the LVC (Low Voltage Control) network. Per the installation guide: ZoneAIR is "designed to provide a single control for multiple fans." You get one Lenze VFD per fan, mounted on the fan frame, with the wiring harness and mounting plate included. A separate ground-level controller (typically an LVC) drives all the fans in the zone together over a daisy-chained 7-wire 18 AWG cable.

## Key Specifications
| Item | Value |
|---|---|
| VFD make | Lenze AC Tech |
| Location | Fan-mounted |
| Fans per VFD | 1 |
| Ground control | Required (typically LVC) |
| Optional internal fire relay | Available |
| Max fans on one LVC | 7 (per ZoneAIR brochure — LVC network limit) |
| Max LVC-to-VFD cable length | 700 ft (214 m) |

## Best Applications
- Multi-fan zones (up to 7 fans on one LVC)
- Agricultural and industrial spaces where all fans in a zone should run from a single ground control
- Installations that want fan-mounted VFDs (short motor cable runs) and analogue/dial-based control
- Single LVC station controlling multiple fans with emergency stop, forward/reverse toggle, and potentiometer speed

## Key Features & Benefits
- Fan-mounted Lenze VFD (mounting plate + wiring harness included)
- Short motor-to-VFD cable run (the VFD is on the fan frame)
- Daisy-chain multiple fans on one LVC
- Emergency stop button on the LVC
- Forward/reverse toggle while in motion
- Speed potentiometer at the LVC station
- Optional TFD-1 temperature controller plugs into the LVC for automated speed control
- Optional internal fire relay
- Optional wind sensor (mandatory in agricultural installs)

## What Makes It Different
- **vs. EssentialAIR:** ZoneAIR is fan-mounted and designed for multi-fan zone control. EssentialAIR is wall-mounted and single-fan.
- **vs. CommandAIR:** both are fan-mounted. CommandAIR is for single-fan installs with a dedicated 100 ft remote keypad. ZoneAIR is for multi-fan zones with an LVC.
- **vs. ModAIR:** ZoneAIR uses LVC (analogue, 0-10 V, 7-wire). ModAIR uses ModBus (digital) and is the path for SmartAIR / TouchAIR. ZoneAIR is simpler; ModAIR is more flexible.

## Power & Electrical Requirements
- Lenze AC Tech VFD (same drive as EssentialAIR and CommandAIR)
- Single-phase input supported on 230 V model (L1-L2 + PE)
- Three-phase: L1-L2-L3 + PE
- Separate insulated ground to each VFD
- Motor insulation class F; no motor thermal wires
- All VFDs in a ZoneAIR system must have their individual power turned on for any fan in the zone to operate
- See `guides/electrical-install-lenze.md` for full current values and cable-length rules

## Mounting & Installation Notes
**Fan mount:** min 1 ft (300 mm) separation between VFD and fan motor. Mounting plate and wiring harness included.

**Conduit rules (shared with EssentialAIR / CommandAIR):**
- Input and output power must not share a conduit
- Control cables must not share a conduit with any power cables
- Different fans' output power cables must not share a conduit
- Different fans' input-only power cables may share a conduit
- **Agricultural / wet environments:** use Wet/Agricultural EMT conduit for both the motor output and the power input runs (in addition to or instead of dry industrial conduit)

**Motor wiring:**
- Nord motor thermal protection wires are **not to be used** — the VFD handles overtemperature and overload protection
- Motor output: AC (PWM) 3Ph (Inverter Duty, 3 wires + insulated ground)
- Power input: 220 VAC, 1PH (2 wires + Ground) on the ZoneAIR schematic

**LVC wiring:**
- 7-wire 18 AWG shielded cable between LVC and the VFDs
- Terminal 6 is not connected between the 1st and 2nd VFD, nor between the 2nd and 3rd VFD
- VFD terminals used: 1, 2, 5, 6, 25, 4, 1, 13A, 13B, 13C, 14, 30, 16, 17
- Max cable distance from LVC to the last VFD: 700 ft (214 m)
- LVC power supply: 240 VAC, 1PH
- Emergency stop connects to the LVC
- TFD-1 (temperature controller) connects to the LVC via 4 wires (18 AWG shielded)

**LVC operating rules:**
1. Do not turn off the fan while in motion using a disconnect switch
2. For manual operation, set the "TFD-1 / Manual" toggle to MANUAL
3. Adjust fan speed with the speed potentiometer
4. Always stop the fan with the red stop button
5. Use the forward/reverse toggle to reverse direction while in motion

**TFD-1 setup** (from ZoneAIR source docs):
- Position 1 (set point): temperature at which the fan begins to run
- Position 2 (modulation band): temperature range over which fan speed ramps from 27 % to 100 %
- Position 3 (minimum ventilation off): temperature below which the fan stops
- Example: set point 20 °C, modulation band 10 °C, min vent off 5 °C → fan starts at 20 °C, full speed at 30 °C, stops at 15 °C
- Minimum programmed speed: 15 Hz / 27 %. Do not lower.

## Maintenance Requirements
- See `guides/maintenance-schedule.md`
- VFD panel check at 12 months, then every 18 months
- Lock out the LVC and the individual VFDs during any fan/mount/guy-wire work

## Compatible Accessories & Controls
- **LVC (Low Voltage Control)** — the main pairing
- **TFD-1 Temperature Controller** — plugs into the LVC
- **Wind Sensor** — integrates with LVC; mandatory in agricultural installs
- **Fire relay** — optional internal Lenze VFD component
- **SmartAIR / TouchAIR** — only if you upgrade the ZoneAIR to ModAIR by adding the ModBus module

## Common FAQs

**Q: How do I stop a ZoneAIR fan safely?**
A: Always use the red stop button on the LVC. Do not use a disconnect switch to stop a running fan.

**Q: What happens if I program the fan below 15 Hz?**
A: The motor will overheat because it cannot draw enough cooling air. This voids the warranty. 15 Hz / 27 % is the hard minimum.

**Q: How many fans can one ZoneAIR + LVC system control?**
A: Up to 7 fans per LVC network, daisy-chained with 7-wire 18 AWG shielded cable, max 700 ft total cable length.

**Q: Can I use SmartAIR or TouchAIR with ZoneAIR?**
A: Not directly. Upgrade ZoneAIR to ModAIR (add the ModBus communications module), or use Schneider VFD instead.

**Q: Does ZoneAIR support single-phase power?**
A: Yes on the 230 V model — use L1-L2 + PE. Three-phase is also supported (L1-L2-L3 + PE).

**Q: What's the minimum VFD-to-fan separation?**
A: 1 ft (300 mm).

**Q: How does the TFD-1 modulation band work?**
A: The fan starts at 27 % (minimum) when the temperature reaches the set point. As temperature rises through the modulation band, the fan ramps linearly to 100 %. When temperature falls, it reverses. The fan stops when temperature drops below (set point – minimum ventilation off temperature).

**Q: Is a wind sensor required?**
A: Mandatory in agricultural installations. Optional for industrial/commercial.

## Source Documents Referenced
- `Electrical Installation Guide 2022 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
