---
id: smartair
name: SmartAIR HMI (single-fan and multi-fan)
type: control
category: hmi
location: wall-mount
fans_controlled: 1 (single-fan) or up to 10 (multi-fan)
interface: touchscreen
power: pulls from Schneider VFD (no separate supply)
requires: schneider-vfd or modair
works_with: [sailfin-geared-8ft, sailfin-geared-12ft, sailfin-geared-16ft, sailfin-geared-20ft, sailfin-geared-24ft, sailfin-gearless-8ft, sailfin-gearless-12ft, sailfin-gearless-16ft, sailfin-gearless-20ft, sailfin-gearless-24ft, schneider-vfd, modair]
source_docs:
  - "Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# SmartAIR HMI (single-fan and multi-fan)

## Overview
SmartAIR is Envira-North's digital touchscreen HMI for Altra-Air Sailfin fans. It runs automatic speed control based on measured temperature and humidity, controls the gearless Sailfin's built-in LED light (on/off and dimming), and integrates with a wind sensor and fire relay. It comes in a single-fan version and a multi-fan version that controls up to 10 fans from one HMI via an RJ45 daisy-chain. SmartAIR requires the Schneider VFD.

## Key Specifications
| Item | Single-fan | Multi-fan |
|---|---|---|
| Max fans | 1 | 10 |
| Requires | Schneider VFD (1 per fan) | Schneider VFD (1 per fan) |
| Power supply | Pulls from the VFD | Supplied to the control box |
| Built-in sensors | Temperature + humidity | Temperature + humidity |
| Interface | Touchscreen | Touchscreen |
| LED light control | Yes (on/off + dimming) | Yes |
| Wind sensor integration | Yes (jumper required if not installed) | Yes |
| Fire relay integration | Yes (jumper required if not installed) | Yes |
| Network | CAT-5 from HMI to VFD | Control box + RJ45 splitters + CAT-5 daisy-chain |
| Auto mode retention on power loss | Not specified for single-fan | Not retentive (resets to Disabled) |

## Best Applications
- Single fan with automated temperature/humidity-based speed control (single-fan version)
- Multi-fan zones up to 10 fans (multi-fan version)
- Facilities with the built-in LED light on a gearless Sailfin (SmartAIR dims and switches the LED)
- Installations that need live drive-data monitoring from ground level
- Facilities with fire suppression (fire relay integration)
- Outdoor-exposed or agricultural installs (wind sensor integration; mandatory jumper otherwise)

## Key Features & Benefits
- **Touchscreen HMI** — auto and manual modes
- **Built-in temperature AND humidity sensors** — the only Envira-North HMI that does humidity
- **Auto mode:** fan starts at the low set point, speed increases linearly up to the high set point. If both temperature and humidity modes are enabled, the fan runs at the higher of the two calculated speeds.
- **Run-below-min option:** optional setting that lets the fan keep running at the low speed % even when temperature is below the low set point.
- **LED light control** — on/off and dimming directly from the HMI (gearless Sailfin only, since geared Sailfins have no LED)
- **Wind sensor alarm display** — fan decelerates on high wind, restarts when wind drops below set point
- **Fire relay alarm display** — fan decelerates on fire alarm, restarts when relay is reset
- **Real-time drive data** — troubleshoot from ground level without climbing to the fan
- **No separate power supply** — the HMI pulls power from the Schneider VFD

## What Makes It Different
- **vs. TouchAIR:** SmartAIR is single-fan or 10-fan; TouchAIR is up to 20 fans and is NEMA4X with BAS in mind.
- **vs. LVC + TFD-1:** SmartAIR is a digital touchscreen with humidity, LED, and real-time data. LVC + TFD-1 is analogue, dial-based, and temperature-only.
- **Requires Schneider VFD.** SmartAIR does not work with Lenze-based control packages unless they are upgraded to ModAIR (Lenze + ModBus).
- **Multi-fan HMI is not retentive on power loss.** If power to the multi-fan HMI is cut, auto-mode settings reset to Disabled and must be re-enabled. This is documented for the multi-fan HMI; the single-fan HMI behaviour is not explicitly specified.

## Power & Electrical Requirements
- SmartAIR HMI pulls power from the Schneider VFD — no separate power supply needed.
- Multi-fan control box has its own power connection on the bottom receiver.
- Wind sensor and fire relay each need a jumper installed if the physical sensor/relay is not connected, or the fan will not operate.

## SmartAIR Screen Descriptions
| Screen | Function |
|---|---|
| Fan Control | Auto/Manual mode, speed, direction selections |
| Light Control | ON/OFF and dimming of the optional LED light (only accessible if LED light option is installed) |
| Main Screen / Auto Mode | Displays sensor readings and current fan speed as calculated from set-points. Selecting this page enters Auto Mode. |
| Settings Screen 1 | Enter set-point values that Auto Mode uses to calculate fan speed |
| Settings Screen 2 | Enable/disable Auto Mode functions (temperature, humidity, Run Below Min) |
| Data Screen | Real-time data from the drive — live monitoring of fan performance |

## SmartAIR Multi-Fan Screen Descriptions
| Screen | Function |
|---|---|
| Fan Control | Auto/Manual mode, speed, direction selections |
| Light Control | ON/OFF and dimming of the optional LED light |
| Main Screen | Sensor readings display |
| System Setting Screen | System-wide settings selection |
| Settings Screen 1 | Set-point values for Auto Mode speed calculation |
| Settings Screen 2 | Enable/disable Auto Mode functions (**NOT retentive — resets to Disabled on power loss**) |
| Data Screen | Real-time data from the drive |

## Mounting & Installation Notes
**HMI placement:**
- Mount in a safe, dry location — not exposed to splashing or washdown
- Avoid direct sunlight, drafts, exterior doorways, skylights, windows, and exterior walls — these affect temperature/humidity accuracy
- Wall-mount with or without an electrical box
- On structural steel columns, use a single-gang weatherproof box to space the HMI off the column and avoid inaccurate temperature readings

**Single-fan CAT-5 connection:**
- Connect CAT-5 to the RJ45 port **inside** the Schneider VFD enclosure — not the external port on the drive
- Use minimum CAT-5 cable
- If more than 100 ft is needed, use bulk CAT-5 with no mid-run couplers

**Multi-fan network setup:**
1. On VFD 1, connect the supplied RJ45 splitter to the short CAT-5 cable inside the VFD
2. Connect the control box's CAT-5 to one port of the splitter
3. Connect a CAT-5 from VFD 1 to VFD 2 on the other splitter port
4. Repeat the splitter pattern for each subsequent VFD
5. The last VFD in the chain does not use a splitter — connect CAT-5 from the previous VFD directly to its internal RJ45 port
6. All CAT-5 connections must be made inside an enclosure
7. Power the control box from the receiver on the bottom

**Multi-fan control box:**
- Mount in a dry location — do not wash with pressurised water
- Provisioned for wind sensor and fire relay — jumpers are installed at the factory if these options were not ordered

## Maintenance Requirements
- See the general Altra-Air Sailfin maintenance schedule in `guides/maintenance-schedule.md`
- VFD panel check at 12 months, then every 18 months
- No maintenance on the controller while powered unless reprogramming or troubleshooting
- Lock out the controller during fan/mount/guy-wire work

## Compatible Accessories & Controls
- **Schneider VFD** (required) — `controls/schneider-vfd.md`
- **Wind Sensor** — integrates directly; jumper required if not installed
- **Fire relay** — optional internal Schneider VFD component; integrates with SmartAIR alarm display
- **Built-in LED light** (on gearless Sailfin) — on/off and dimming from the HMI

## Common FAQs

**Q: Does SmartAIR auto mode work with both temperature and humidity?**
A: Yes. When both are enabled, the fan runs at the higher of the two calculated speeds. Each can also be enabled independently.

**Q: What happens if I lose power to the multi-fan HMI?**
A: Auto-mode settings reset to Disabled. You must re-enable them when power is restored. This is documented for the multi-fan HMI specifically; the single-fan HMI behaviour is not explicitly stated.

**Q: How many fans can one SmartAIR HMI control?**
A: 1 with the standard SmartAIR, or up to 10 with the SmartAIR Multi-Fan option.

**Q: Do I need a separate power supply for the HMI?**
A: No — the SmartAIR HMI pulls power from the Schneider VFD.

**Q: Where does the CAT-5 connect?**
A: To the internal RJ45 port inside the Schneider VFD enclosure. Do not use the external RJ45 port on the drive.

**Q: What happens if I don't install a wind sensor or fire relay but leave out the jumper?**
A: The fan will not operate. A jumper must be installed in place of any sensor/relay that is not connected.

**Q: Can SmartAIR dim the built-in LED?**
A: Yes — on/off and dimming from the HMI. On 240 V models, the light L1/L2 can connect directly to the VFD L1/L2 input. On **480 V models**, the LED light must be supplied from an **external 120 V or 240 V source**. Compatible external dimmer switches (for non-HMI dimming): **Leviton DS710-10Z** or **Lutron DVSTV-WH** (0-10V LED compatible). A standard 120 VAC switch can be used for ON/OFF only at 100% brightness (no dimming).

**Q: Does SmartAIR work with Lenze-based control packages?**
A: Yes — when those Lenze drives are configured as **ModAIR** (Lenze VFD + ModBus Communications Module). The Control Options brochure (2023) explicitly states SmartAIR is "designed to work in conjunction with Schneider VFDs, ModAIR Fan Controls, or a mixture of both options." Standard Lenze-only packages (EssentialAIR, ZoneAIR, CommandAIR without ModBus) are not compatible.

**Q: Is SmartAIR compatible with Jazz fans?**
A: No. Jazz fans must be on their own separate network with their own Jazz HMI. TouchAIR can supervise a Jazz zone, but SmartAIR cannot.

## Source Documents Referenced
- `Electrical Installation Guide - Schneider Drive - 2023-09142023- FullDocument-Version8 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
