---
id: electrical-install-lenze
name: Sailfin Fan Electrical Installation — Lenze AC Tech Drive Path (EssentialAIR / ZoneAIR / CommandAIR)
type: guide
category: electrical
applies_to: [sailfin-geared, sailfin-gearless, essentialair, zoneair, commandair, lvc, tfd-1]
source_docs:
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
  - "Electrical Installation Guide 2022 (1) (pdfplumber).txt"
last_verified: 2026-04-11
---

# Sailfin Fan Electrical Installation — Lenze AC Tech Drive Path

## Overview
This guide is sourced from the **Electrical Installation Guide — Altra-Air Sailfin Fan (2022)**, which covers EssentialAIR, ZoneAIR, and CommandAIR control installations for the Sailfin fan. It covers electrical installation rules that apply when a Sailfin fan is controlled through a Lenze AC Tech VFD. For ModAIR (Lenze + ModBus), the same VFD wiring rules apply but consult Envira-North for ModBus-specific wiring. For the Schneider path (SmartAIR / TouchAIR), see `guides/electrical-install-schneider.md`.

## Safety Precautions
- All installations must be performed by a **qualified person**.
- Do not work on live equipment. **Use of lock-out procedures is a must.**
- **IMPORTANT:** The installation of a wind sensor is **mandatory in all agricultural installations.**
- All installation wiring must conform to the National Electrical Code and meet local codes. Code compliance is ultimately the installer's and/or the user's responsibility.

## Package Contents by Control Type
| Control Type | Included Items |
|---|---|
| EssentialAIR | Lenze AC Tech VFD only (wall-mounted) |
| ZoneAIR | Lenze VFD + Mounting Plate + Wiring Harness |
| CommandAIR | Lenze VFD + Mounting Plate + Wiring Harness + Control Wire + 100 ft (30.48 m) CAT-5 + Remote Keypad |

## Power feed to the VFD
- **Voltages supported:** 230 V (240 V), 400 V, 460 V (480 V), 600 V — single-phase supported at 230 V only
- **One VFD per fan**
- **Mounting:** the Lenze VFD is fan-mounted for ZoneAIR / CommandAIR / ModAIR; wall-mounted remote for EssentialAIR
- **Disconnect:** local lockable disconnect within sight of the drive (not provided with the package)

## Power requirements — full-load current values

All values are full-load current. Wire sizing must meet NEC and local codes.

| Motor HP (kW) | INPUT 240 V — 1Ph | INPUT 240 V — 3Ph | OUTPUT 240 V — 3Ph | INPUT 400 V — 3Ph | OUTPUT 400 V — 3Ph | INPUT 480 V — 3Ph | OUTPUT 480 V — 3Ph | INPUT 600 V — 3Ph | OUTPUT 600 V — 3Ph |
|---|---|---|---|---|---|---|---|---|---|
| 1.0 HP (0.75 kW) | 8.8 A | 5.0 A | 4.2 A | 2.9 A | 2.4 A | 2.5 A | 2.1 A | 2.0 A | 1.7 A |
| 1.5 HP (1.1 kW) | 12.0 A | 6.9 A | 6.0 A | 4.2 A | 3.5 A | 3.6 A | 3.0 A | N/A | N/A |
| 2.0 HP (1.5 kW) | 13.3 A | 8.1 A | 7.0 A | 4.7 A | 4.0 A | 4.1 A | 3.5 A | 3.2 A | 2.7 A |

**Voltage operating ranges:**
- 240 V: 170–264 VAC, 48–62 Hz
- 400 V: 340–440 VAC, 48–62 Hz
- 480 V: 340–528 VAC, 48–62 Hz
- 600 V: 425–660 VAC, 48–62 Hz

**HP by Sailfin size:**
- 1.0 HP: Sailfin Geared 8 FT, 12 FT
- 1.5 HP: Sailfin Geared 16 FT
- 2.0 HP: Sailfin Geared 20 FT, 24 FT; all Sailfin Gearless sizes

A separate insulated ground must run from the electrical panel to each VFD.

## Wiring Schematic Notes
- Maintain a minimum distance of **1 ft (300 mm)** between the VFD and the fan motor.
- **Motor output conduit:** dry industrial/commercial conduit (Inverter Duty, 3 wires + insulated ground)
- **Power input conduit:**
  - Single-phase (230 V model only): 2 wires + insulated ground
  - Three-phase: 3 wires + insulated ground
- **ZoneAIR wiring schematic additionally requires:**
  - Wet/Agricultural EMT conduit on both the motor output and power input sides (agricultural environments)
  - 220 VAC, 1PH input (2 wires + Ground) — ZoneAIR-specific supply wiring
  - 7-wire 18 AWG shielded cable to the LVC / Temperature Control / Wind Sensor
  - See Wind Sensor Manual for installation details

## Wire Connections (VFD Input Power)
- **Single-phase (1Ph):** use L1 - L2 + PE (Ground)
- **Three-phase (3Ph):** use L1 - L2 - L3 + PE (Ground)

## Wire Connections (Motor)
- The thermal protection wires in the junction box of the Nord motor are **not to be used** unless otherwise directed. The VFD provides over-temperature and overload protection.
- **Motor terminal connections by voltage:**

| Voltage | Terminals |
|---|---|
| 460 VAC | T1 - T2 - T3 (per 460V label) |
| 400 VAC | T1 - T2 - T3 (per 400V label) |
| 230 VAC | T1 - T2 - T3 (per 230V label) |

## Motor cable length limits (critical)

Three tiers depending on run length:

| Tier | 230 VAC | 460 VAC | 600 VAC | Action |
|---|---|---|---|---|
| Normal | Up to 250 ft | Up to 160 ft | Up to 125 ft | No extra device, no HP change |
| Extended | 250–400 ft | 160–250 ft | 125–160 ft | Load reactor required (1.5 % or 3 % impedance) |
| Long run | 400–1000 ft | 250–1000 ft | 160–1000 ft | dV/dT filter required + upsize VFD by +1 HP |

Load reactor or dV/dT filter must be installed within 6–10 ft of the VFD on the load side.

> **600 V note:** excessive reflected voltages at 600 V can shorten motor and VFD life and cause bearing failures. Follow the table strictly at this voltage.

Consult Envira-North Customer Support for sizing the reactor or filter for a specific run.

## Control wiring — LVC (0–10 V analogue)
- **ZoneAIR / LVC path:** 7-wire cable, up to 7 fans, 700 ft max total run
- **LVC to Schneider VFD (mixed analogue path):** 6-wire cable, up to 10 fans, 1000 ft max total run
- **Wire gauge:** 18 AWG shielded for TFD-1 to LVC (4 wires)
- **Shield:** ground the shield at the LVC end only (single-point ground to avoid ground loops)

### LVC Terminal Wiring (ZoneAIR)
- VFD terminals used for LVC connections: **1, 2, 5, 6, 25, 4, 1, 13A, 13B, 13C, 14, 30, 16, 17**
- **Terminal 6 is NOT connected** between the 1st and 2nd VFD, nor between the 2nd and 3rd VFD
- **All VFDs must have their individual power turned on** for any fans in the zone to operate
- LVC connects to: 7-wire 18 AWG shielded (to VFDs) + 4-wire 18 AWG shielded (to TFD-1)
- LVC power supply: **240 VAC, 1PH**
- Emergency stop is wired to the LVC
- Maximum distance from the LVC to the last VFD: **700 ft (214 m)**

## Control wiring — CommandAIR / ModAIR
- **CommandAIR:** 100 ft CAT-5 from the fan-mounted VFD to a remote keypad — single fan only
- **ModAIR:** ModBus RTU from the fan-mounted VFD to a SmartAIR or TouchAIR HMI — lets a Schneider-network HMI command a Lenze-drive fan
- **EssentialAIR:** no separate control cable — the Lenze drive itself is wall-mounted and operated directly

## Minimum fan speed (hard limit)
- **15 Hz / 27 %** — do NOT program lower
- Below this speed the motor does not move enough air to cool itself and will overheat
- Running below 15 Hz voids the warranty

## Wind sensor and fire relay (LVC path)
- Wind sensor wires to the LVC analogue input
- Fire relay wires to the LVC (or to each individual VFD as a per-fan option)
- See `controls/wind-sensor.md` and `controls/lvc.md`

## Grounding and separation
- Bond VFD enclosure and fan structure to building ground
- Keep 0–10 V control wiring away from motor power cables (different conduits)
- Twisted-pair shielded cable recommended for long LVC runs near power wiring

## Operating Instructions

### EssentialAIR Keypad Operation
The EssentialAIR is operated directly from the Lenze drive keypad:
- **TO START:** Press the Start button
- **TO STOP:** Press the Stop button
- **TO CHANGE SPEED:** Press the speed up/down buttons
- **TO CHANGE ROTATION:** Press the direction button, then press Start

### CommandAIR Remote Keypad Operation
The CommandAIR uses a remote keypad connected via 100 ft CAT-5 cable. The same operations apply:
- **TO START:** Press the Start button
- **TO STOP:** Press the Stop button
- **TO CHANGE SPEED:** Press the speed buttons
- **TO CHANGE ROTATION:** Press the direction button, then press Start

### LVC Operating Instructions (ZoneAIR Manual Mode)
1. **DO NOT turn off the fan while in motion using a disconnect switch.**
2. Set the "TFD-1 / Manual" toggle to the **MANUAL** position.
3. Use the speed potentiometer to adjust the fan's speed.
4. Always use the **Red Stop button** (on the right of the Low Voltage Controller) to turn off or stop the fan.
5. To reverse direction while the fan is in motion, use the "Forward / Reverse" toggle.

### LVC + TFD-1 Operating Instructions (ZoneAIR Automatic Mode)
1. **DO NOT turn off the fan while in motion using a disconnect switch.**
2. Set the "TFD-1 / Manual" toggle to the **TFD-1** position.
3. Always use the **Red Stop button** to turn off or stop the fan.
4. To reverse direction while the fan is in motion, use the "Forward / Reverse" toggle.

## Start-up sequence
1. Verify cable-length limits and load reactor / dV/dT filter if applicable
2. Verify minimum speed is not set below 15 Hz
3. Apply power to each VFD
4. Apply power to the LVC / HMI
5. If using TFD-1, set the "TFD-1 / Manual" toggle to MANUAL and verify with the speed potentiometer
6. Switch to TFD-1 and confirm set-point / modulation-band / min-vent-off behaviour
7. Commission wind sensor trigger before the first season of outdoor use

## Common pitfalls
- **Cable too long without a reactor** — causes reflected-wave overvoltage and premature motor failure
- **Minimum speed set below 15 Hz** — motor overheats, warranty voided
- **Shield grounded at both ends** — ground loop on the 0–10 V signal
- **Unshielded 4-wire to TFD-1** — use 18 AWG shielded
- **Mixing Jazz on the LVC network** — not supported, Jazz is its own network

## Source Documents Referenced
- `Electrical Installation Guide 2022 (pdfplumber).txt`
- `Electrical Installation Guide 2022 (1) (pdfplumber).txt` (identical content — verified)
