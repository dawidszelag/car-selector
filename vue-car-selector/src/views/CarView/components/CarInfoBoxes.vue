<template>
  <div class="top-container" style="margin-top: 40px;">
    <div class="top">
      <div> ${{ Formatter.formatPrice(car.price_au) }}</div>
      <span class="section-text-subtitle">price</span>
    </div>
    <div class="top">
      <div> {{ car.warranty_years_au ?? '--' }} {{ car.warranty_years_au === 1 ? 'YEAR' : 'YEARS' }}</div>
      <span class="section-text-subtitle">WARRANTY</span>
    </div>
    <div class="top">
      <div class="stars">
        <div v-for="index in car.ancap ?? 5" :key="index">
          ★
        </div>
      </div>
      <span class="section-text-subtitle">ANCAP SAFETY RATING</span>
    </div>
  </div>
  <div class="top-container">
    <div class="top-bottom" v-for="item in CAR_SUMMARY" :key="item.name">
      <div>{{ item.value.toUpperCase() }}</div>
      <span class="section-text-subtitle">{{ item.name.toUpperCase() }}</span>
    </div>
  </div>
</template>

<script setup>
import {computed, defineProps} from "vue";
import {DriveType, FuelType, FuelTypeEnum} from "../../../dicts";
import {Formatter} from "../../../utils";

const props = defineProps(['car']);

const { car } = props;
const DEFAULT_SUMMARY = [
  {
    name: "FUEL TYPE",
    value: `${FuelType[car.fuel_type] ?? '--'}`
  },
  {
    name: "ENGINE SIZE",
    value: `${car.engine_size ?? '--'} cm3`
  },
  {
    name: "POWER",
    value: `${car.power_kw ?? '--'} kW / ${car.power_hp ?? '--'} HP`
  },
  {
    name: "DRIVE",
    value: `${DriveType[car.drive] ?? '--'}`
  },
]

const ELECTRIC_SUMMARY = [
  {
    name: "FUEL TYPE",
    value: `${FuelType[car.fuel_type] ?? '--'}`
  },
  {
    name: "RANGE (MAX)",
    value: `${car.electric_range ?? '--'} km`
  },
  {
    name: "POWER",
    value: `${car.power_kw ?? '--'} kW / ${car.power_hp ?? '--'} HP`
  },
  {
    name: "DRIVE",
    value: `${DriveType[car.drive] ?? '--'}`
  },
]


const CAR_SUMMARY= computed(() => {
  if (car.fuel_type === FuelTypeEnum.ELECTRIC) return ELECTRIC_SUMMARY
  return DEFAULT_SUMMARY
})
</script>

<style scoped>
.top-container {
  display: flex;
  justify-content: space-between;
}

.top-bottom,
.top {
  width: 35%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  padding: 15px 3px;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
  font-weight: 600;
  font-size: 21px;
  border-width: 3px;
  border-style: solid;
  border-image: linear-gradient(rgba(215, 29, 128, 0.8), rgba(196, 44, 135, 0.8)) 30;
  border-top: none;
}
.top-bottom {
  font-size: 17px;
  text-align: center;
}


span {
  text-transform: uppercase;
  display: block;
  font-size: 12px;
}


.top:first-child {
  border-left-width: 6px;
  border-left-style: solid;
  border-image: linear-gradient(rgba(215, 29, 128, 0.8), rgba(196, 44, 140, 0.8)) 30;
}

.top:last-child {
  border-right-width: 6px;
  border-right-style: solid;
  border-image: linear-gradient(rgba(215, 29, 128, 0.8), rgba(196, 44, 140, 0.8)) 30;
}

.top-bottom {
  border-width: 3px;
  border-style: solid;
  border-image: linear-gradient(rgba(215, 29, 128, 0.8), rgba(196, 44, 140, 0.8)) 30;
  border-bottom: none;
  background: rgba(255, 255, 255, 0.04);
}

.top-bottom:first-child {
  border-left: none;
}

.top-bottom:last-child {
  border-right: none;
}

.stars {
  display: flex;
  font-size: 19px;
  padding: 2px;
}
</style>