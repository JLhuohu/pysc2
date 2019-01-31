# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Define the static list of upgrades for SC2."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import enum


# pylint: disable=invalid-name
class Upgrades(enum.IntEnum):
  """The list of upgrades, as generated by bin/gen_data.py."""
  AdeptPiercingAttack = 130
  AnabolicSynthesis = 88
  BansheeCloak = 20
  BansheeSpeed = 136
  BattlecruiserEnableSpecializations = 76
  BlinkTech = 87
  Burrow = 64
  CarrierLaunchSpeedUpgrade = 1
  CentrificalHooks = 75
  Charge = 86
  ChitinousPlating = 4
  CycloneLockOnDamage = 144
  CycloneRapidFireLaunchers = 291
  DarkTemplarBlinkUpgrade = 141
  DiggingClaws = 293
  DrillClaws = 122
  EvolveGroovedSpines = 134
  EvolveMuscularAugments = 135
  ExtendedThermalLance = 50
  GlialReconstitution = 2
  GraviticDrive = 49
  HiSecAutoTracking = 5
  HighCapacityBarrels = 19
  InfestorEnergyUpgrade = 74
  LiberatorAGRangeUpgrade = 140
  MedivacIncreaseSpeedBoost = 139
  NeosteelFrame = 10
  NeuralParasite = 101
  ObserverGraviticBooster = 48
  OverlordSpeed = 62
  PersonalCloaking = 25
  PhoenixRangeUpgrade = 99
  ProtossAirArmorsLevel1 = 81
  ProtossAirArmorsLevel2 = 82
  ProtossAirArmorsLevel3 = 83
  ProtossAirWeaponsLevel1 = 78
  ProtossAirWeaponsLevel2 = 79
  ProtossAirWeaponsLevel3 = 80
  ProtossGroundArmorsLevel1 = 42
  ProtossGroundArmorsLevel2 = 43
  ProtossGroundArmorsLevel3 = 44
  ProtossGroundWeaponsLevel1 = 39
  ProtossGroundWeaponsLevel2 = 40
  ProtossGroundWeaponsLevel3 = 41
  ProtossShieldsLevel1 = 45
  ProtossShieldsLevel2 = 46
  ProtossShieldsLevel3 = 47
  PsiStormTech = 52
  PunisherGrenades = 17
  RavenCorvidReactor = 22
  ShieldWall = 16
  SmartServos = 289
  Stimpack = 15
  TerranBuildingArmor = 6
  TerranInfantryArmorsLevel1 = 11
  TerranInfantryArmorsLevel2 = 12
  TerranInfantryArmorsLevel3 = 13
  TerranInfantryWeaponsLevel1 = 7
  TerranInfantryWeaponsLevel2 = 8
  TerranInfantryWeaponsLevel3 = 9
  TerranShipWeaponsLevel1 = 36
  TerranShipWeaponsLevel2 = 37
  TerranShipWeaponsLevel3 = 38
  TerranVehicleAndShipArmorsLevel1 = 116
  TerranVehicleAndShipArmorsLevel2 = 117
  TerranVehicleAndShipArmorsLevel3 = 118
  TerranVehicleWeaponsLevel1 = 30
  TerranVehicleWeaponsLevel2 = 31
  TerranVehicleWeaponsLevel3 = 32
  TunnelingClaws = 3
  WarpGateResearch = 84
  ZergFlyerArmorsLevel1 = 71
  ZergFlyerArmorsLevel2 = 72
  ZergFlyerArmorsLevel3 = 73
  ZergFlyerWeaponsLevel1 = 68
  ZergFlyerWeaponsLevel2 = 69
  ZergFlyerWeaponsLevel3 = 70
  ZergGroundArmorsLevel1 = 56
  ZergGroundArmorsLevel2 = 57
  ZergGroundArmorsLevel3 = 58
  ZerglingAttackSpeed = 65
  ZerglingMovementSpeed = 66
  ZergMeleeWeaponsLevel1 = 53
  ZergMeleeWeaponsLevel2 = 54
  ZergMeleeWeaponsLevel3 = 55
  ZergMissileWeaponsLevel1 = 59
  ZergMissileWeaponsLevel2 = 60
  ZergMissileWeaponsLevel3 = 61
