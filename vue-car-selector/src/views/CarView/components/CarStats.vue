<template>
  <div class="top-container" style="margin-top: 40px;">
    <div v-for="stat in CAR_STATS" class="stats">
      <div class="section-text-d">{{ stat.title }}</div>
      <div class="section-text-subtitle">{{ stat.subtitle }}</div>
      <div class="currentValue">
        <div :style="{width: `${(stat.value/stat.max)*100}%`}" class="value"></div>
        <span>{{ stat.textValue }}</span>
      </div>
      <div :style="{width: '100%'}" class="maxValue"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {computed, defineProps, PropType} from "vue";
import {FuelTypeEnum} from "../../../dicts";
import {DataTime} from "../../../utils";
import type {CarDetailsOut} from "../../../api";

const props = defineProps({
  car: {
    type: Object as PropType<CarDetailsOut>,
    required: true
  }
});

const ELECTRIC = [
  {
    max: props.car.stats?.max_electric_charging_time,
    value: props.car.charging_time,
    textValue: DataTime.convertToTime(props.car.charging_time * 60),
    title: "CHARGING TIME",
    subtitle: "0 - 100% @ 7.4 kWH"
  },
  {
    max: props.car.stats?.max_electric_fast_charging_time,
    value: props.car.fast_charging_time,
    textValue: DataTime.convertToTime(props.car.fast_charging_time),
    title: "FAST CHARGING",
    subtitle: "10-80% @ 150 kWh"
  }
]
const PETROL_CAR = [
  {
    max: props.car.stats?.max_fuel_range,
    value: props.car.fuel_average_distance,
    textValue: (props.car.fuel_average_distance || '--')+ ' KM',
    title: "AVERAGE FUEL RANGE",
    subtitle: "KM"
  },
  {
    max: props.car.stats?.max_fuel_efficiency,
    value: props.car.fuel_combined,
    textValue: (props.car.fuel_combined || '--') + ' L',
    title: "FUEL EFFICIENCY",
    subtitle: "L/100KM"
  }
];
const PHEV = [
  {
    max: props.car.stats?.max_hybrid_range,
    value: props.car.electric_range,
    textValue: (props.car.electric_range || '--') + ' KM' ,
    title: "MAXIMUM ELECTRIC RANGE",
    subtitle: "KM"
  },
  {
    max: props.car.stats?.max_hybrid_charging_time,
    value: props.car.charging_time,
    textValue: DataTime.convertToTime(props.car.charging_time * 60),
    title: "CHARGING TIME",
    subtitle: "0 - 100% @ 7.4 kWH"
  }
];

const CAR_STATS = computed(() => {
  if (props.car.fuel_type === FuelTypeEnum.ELECTRIC) return ELECTRIC
  if (props.car.fuel_type === FuelTypeEnum.PHEV) return PHEV
  return PETROL_CAR
})
</script>

<style scoped lang="less">
.stats {
  margin-top: 20px;
}

.section-text-d {
  margin-bottom: 0;
}

.value, .maxValue {
  display: inline-block;
  height: 8px;
  background: rgba(36, 36, 36, 0.6);
}

.value {
  background: linear-gradient(to right, rgba(215, 29, 128, 0.57), rgba(173, 63, 133, 0.8));
}

.currentValue div {
  margin-right: 15px;

}
span{
  position: absolute;
}
</style>