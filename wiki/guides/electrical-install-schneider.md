---
id: electrical-install-schneider
name: Electrical Installation — Schneider Drive Path
type: guide
category: electrical
applies_to: [sailfin-geared, sailfin-gearless, schneider-vfd, smartair, smartair-multifan, touchair]
source_docs:
  - "Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt"
last_verified: 2026-04-11
---

# Electrical Installation — Schneider Drive Path

## Overview
This guide covers the electrical installation rules that apply when a Sailfin fan (geared or gearless) is controlled through a Schneider VFD — the network used by SmartAIR, SmartAIR Multi-Fan, and TouchAIR. For the Lenze AC Tech path (EssentialAIR / ZoneAIR / CommandAIR / ModAIR), see `guides/electrical-install-lenze.md`.

## Safety Precautions
- All installations must be performed by a **qualified person**.
- Do not work on live equipment. **Use of lock-out procedures is a must.**
- **IMPORTANT:** The installation of a wind sensor is **mandatory in all agricultural installations.**
- All installation wiring must conform to the National Electrical Code and meet local codes. Code compliance is ultimately the installer's and/or the user's responsibility.
- Subject to changes without notification.

## Included Components (General Electrical Installation)
- Fan Mounted VFD
- VFD Mounting Plate and Fasteners
- 100 ft CAT-5 Cable

## Included Components (SmartAIR Single-Fan)
- SmartAIR Graphic Interface (HMI)
- RJ45 Coupler
- 100 ft CAT-5 Cable
- Split Cable Gland

## Included Components (SmartAIR Multi-Fan)
- HMI Control
- Control Box
- RJ45 Splitters
- 100 ft CAT-5 Cable

## Who should read this
- Electricians commissioning a new SmartAIR / TouchAIR installation
- Project managers specifying control wiring in a design-build
- Service technicians troubleshooting drive-to-HMI communication

## Power feed to the VFD
- **Voltages supported:** 200–240 V, 380–500 V, 525–600 V (single- or three-phase capable per catalogue)
- **One VFD per fan** — each Schneider drive controls exactly one motor. Do not parallel two motors on one drive.
- **Mounting:** the Schneider VFD is fan-mounted (bolted to the fan column / motor housing), NEMA4X rated
- **Disconnect:** a local lockable disconnect is required within sight of the drive per NEC 430.102 (not provided)
- **Wire requirements:**
  - Wire size depends on the length and current draw of the VFD and motor
  - Use a continuous run of wires between the motor and VFD — no splices or connections
  - Use adequately sized, **shielded VFD cables** for VFD-to-motor wiring
  - Separate insulated ground must be provided to each VFD from the electrical panel
  - Motor is rated with Insulation Class F — ensure proper wiring per current electrical codes

## Wire Connections (VFD Input Power)
- **Single-phase (1Ph):** use L1 - L2 + PE (Ground)
- **Three-phase (3Ph):** use L1 - L2 - L3 + PE (Ground)

## Wire Connections (Motor)
- The VFD provides over-temperature and overload protection.
- **Motor terminal connections by voltage:**

| Voltage | Terminals |
|---|---|
| 460 VAC | T1 - T2 - T3 (per 460V label) |
| 230 VAC | T1 - T2 - T3 (per 230V label) |

## Communication wiring (VFD ↔ HMI)
- **Cable:** CAT-5 (or CAT-5e), made off with RJ45 connectors
- **Internal RJ45 only** — every connection must land inside an enclosure. Never use the external RJ45 port on the drive as a connection point.
- **Single-fan SmartAIR:** direct HMI-to-VFD run. HMI pulls power from the VFD over the CAT-5.
- **Multi-fan SmartAIR:** star from the control box to VFD #1, then daisy-chain VFD-to-VFD through RJ45 splitters inside each VFD enclosure. The last VFD in the chain does not use a splitter.
- **Control box (multi-fan):** mount dry, do not pressure-wash. Wind sensor and fire relay landings are provisioned at the factory — if either was not ordered, a jumper occupies the position and must remain in place.

## LED Light Wiring (Optional)
If the fan is fitted with the optional LED light, it can be controlled through the VFD via the SmartAIR HMI or by a separate ON/OFF/Dimmer switch.

### SmartAIR LED Control (wired through VFD)
- Wire the LED light to the drive as per the installation guide to allow ON/OFF and dimming control from the HMI.
- A junction box and additional wire may be required depending on the VFD mounting location.
- **240 V models only:** the Light L1/L2 may be connected to the L1/L2 input of the VFD.
- **480 V models:** the LED light **must** be supplied from an external 120 V or 240 V source — the VFD input cannot be used to power the light.

### External Switch — Without Dimming
- A standard 120 VAC light switch provides ON/OFF control only (no dimming).
- The light will operate at **100% brightness** when switched ON if no dimmer is connected.

### External Switch — With Dimming
- A **0-10 V LED compatible dimmer switch** must be used for dimming control.
- Compatible dimmer models: **Leviton DS710-10Z** or **Lutron DVSTV-WH**

## LVC Wiring (Schneider VFD — Optional)
- Daisy-chain all **6 control wires** from the 1st VFD to the 2nd VFD and repeat for all VFDs on the network.
- **Maximum 10 VFDs** per LVC network.
- Use **shielded cable, 18 AWG minimum**.
- **Maximum system cable length: 1000 ft (305 m).**

## Wind sensor and fire relay
- **Wind sensor:** mandatory in agricultural installations. If not installed, a jumper must occupy its position or the fan will not operate.
- **Fire relay:** optional. If not installed, a jumper must occupy its position or the fan will not operate.
- See `controls/wind-sensor.md` for trigger behaviour.

## Grounding and bonding
- Bond the VFD enclosure to building ground per local code
- Bond the fan structure (column / hub) to building ground — the Sailfin safety cable is a secondary restraint, not an electrical bond
- Follow the Schneider drive manual for PE / earth terminal torque

## SmartAIR HMI Installation Considerations
- The HMI must be mounted in a **safe and dry location**.
- Do not mount in a location exposed to direct liquid contact (splashing or washdown).
- If using the built-in temperature and/or humidity sensors, HMI placement is critical for accurate readings:
  - Avoid direct sunlight, drafts, exterior doorways, skylights, windows, and exterior walls.
- Can be mounted directly to a wall with or without an electrical box.
- On structural steel columns, use a **single gang weatherproof box** to space the HMI off the column (prevents inaccurate temperature readings).

## SmartAIR Auto Mode Operation
### Settings Screen 2 — Control Modes
- **Units:** select °C or °F for displayed temperature.
- **Auto Mode:** when enabled, the fan automatically starts when temperature or humidity rises to the Low Temp/RH set-point, beginning at the Low Speed % set-point. Speed increases linearly to the High Speed % as temperature/humidity rises to the High Temp/RH set-point. At or above the High Temp/RH set-point, the fan runs at High Speed %.
- If both Temperature and Humidity Auto Modes are enabled, the fan runs at the **higher of the two calculated speeds**.
- **Run Below Min:** allows the fan to continue running at the Low Speed % set-point even if the sensed temperature is below the Low Temp set-point.

### SmartAIR Multi-Fan Settings Note
- Settings on the Settings Screen 2 are **not retentive**. If power to the HMI is lost, they reset to Disabled and must be re-enabled for the fan to function in Auto Mode.

## Separation rules
- Do NOT run the CAT-5 communication cable in the same conduit as the motor power cable
- Keep control and power cables separated per standard VFD EMC practice
- The Schneider drive is fan-mounted so the motor cable is short — no cable-length derating table applies (this is a Lenze-path concern, not Schneider)

## Start-up sequence
1. Verify all enclosures are closed and torqued
2. Verify all jumpers (wind / fire) are in place if the real device was not ordered
3. Apply power to the VFD
4. Apply power to the HMI / control box
5. Confirm HMI boots and reads live drive data
6. Run the fan up to full speed in manual mode
7. Enable auto mode only after manual operation is verified

## Common pitfalls
- **External RJ45 used** — violates the "inside an enclosure only" rule. Re-terminate inside the VFD.
- **Missing jumper** — if the wind sensor or fire relay position is empty, the fan will not run. Install the jumper or the real device.
- **Mixed networks** — never connect a Jazz fan to a Schneider/SmartAIR network. Jazz is on its own protocol.
- **Auto-mode reset after power loss (multi-fan)** — expected behaviour. Operators must re-enable auto mode after a power interruption.

## Source Documents Referenced
- `Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt`
