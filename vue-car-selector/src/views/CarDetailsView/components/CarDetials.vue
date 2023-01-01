<template>
  <div class="details-box">
    <ul v-for="section in CAR_DETAILS">
      <li v-for="item in section">
        <div class="name">{{ item.name }}</div>
        <div class="value">{{ item.value }}</div>
      </li>
    </ul>
    <ul>
      <li>
        <div class="name">ANCAP - SAFETY RATINGS</div>
        <div class="value">{{ car.ancap }}/5</div>
      </li>
      <li>
        <div class="name">SAFETY ADULT</div>
        <div class="value">{{ car.safety_adult ?? '--' }}/100</div>
      </li>
      <li>
        <div class="name">SAFETY CHILD</div>
        <div class="value">{{ car.safety_child ?? '--' }}/100</div>
      </li>
      <li>
        <div class="name">SAFETY PEDESTRIAN PROTECTION</div>
        <div class="value">{{ car.safety_road_user ?? '--' }}/100</div>
      </li>
      <li>
        <div class="name">SAFETY SYSTEMS</div>
        <div class="value">{{ car.safety_systems ?? '--' }}/100</div>
      </li>
    </ul>
    <ul>
      <li>
        <div class="name">WARRANTY (YEARS)</div>
        <div class="value">{{ car.warranty_years ?? '--' }}</div>
      </li>
      <li>
        <div class="name">WARRANTY (KM)</div>
        <div class="value">{{ car.warranty_distance ?? '--' }}</div>
      </li>
    </ul>

    <ul>
      <li>
        <div class="name">BODY</div>
        <div class="value">{{ car.body.name ?? '--' }}</div>
      </li>
      <li>
        <div class="name">DOORS</div>
        <div class="value">{{ car.doors ?? '--' }}</div>
      </li>
      <li>
        <div class="name">SEATS</div>
        <div class="value">{{ car.seats ?? '--' }}</div>
      </li>
      <li>
        <div class="name">MINIMUM BOOT SPACE</div>
        <div class="value">{{ car.min_boot_space ?? '--' }}</div>
      </li>
      <li>
        <div class="name">MAXIMUM BOOT SPACE</div>
        <div class="value">{{ car.max_boot_space ?? '--' }}</div>
      </li>
    </ul>
    <ul>
      <li>
        <div class="name">LENGTH</div>
        <div class="value">{{ car.length ?? '--' }}mm</div>
      </li>
      <li>
        <div class="name">WIDTH</div>
        <div class="value">{{ car.width ?? '--' }}mm</div>
      </li>
      <li>
        <div class="name">HEIGHT</div>
        <div class="value">{{ car.height ?? '--' }}mm</div>
      </li>
      <li>
        <div class="name">TARE MASS (KG)</div>
        <div class="value">{{ car.tare_mass ?? '--' }}</div>
      </li>
      <li>
        <div class="name">GROUND CLEARANCE</div>
        <div class="value">{{ car.ground_clearance ?? '--' }}mm</div>
      </li>
    </ul>

  </div>
</template>

<script setup>
import {computed, defineProps} from "vue";
import {DriveType, FuelType, FuelTypeEnum} from "../../../dicts";

const props = defineProps(['car']);

const {car} = props;

const formatPrice = (value) => {
  let val = (value / 1).toFixed(0).replace('.', ',')
  return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
}

const convertToTime = (number) => {
  const hour = number ? parseInt(car.fast_charging_time / 60) : 0
  const min = number ? parseInt(car.fast_charging_time % 60) : 0
  return `${hour}h${min}min`
}


const PHEV = [
  [
    {
      name: "ENGINE SIZE",
      value: `${car.engine_size ?? '--'} cm3`
    },
    {
      name: "CYLINDERS &  ENGINE CONFIGURATION",
      value: `${car.cylinders ?? '--'} ${car.engine_configuration ?? '--'} `
    },
    {
      name: "POWER (kW/HP) + POWER (rpm)",
      value: `${car.power_kw ?? '--'} kW/${car.power_hp ?? '--'} hp @ ${car.power_rpm ?? '--'} rpm `
    },
    {
      name: "TORQUE + TORQUE Nm",
      value: `${car.torque_nm ?? '--'} Nm @ ${car.torque_rpm ?? '--'} rpm`
    },
  ],
  [
    {
      name: "ACCELERATION 0 - 100 km/h",
      value: `${car.acceleration ?? '--'} sec`
    },
    {
      name: "TOP SPEED",
      value: `${car.top_speed ?? '--'} km/h`
    }
  ],
  [
    {
      name: "DRIVE",
      value: `${DriveType[car.drive] ?? '--'}`
    },
    {
      name: "TRANSMISSION",
      value: `${car.transmission ?? '--'}`
    }],
  {
    name: "GEARS",
    value: `${car.gears ?? '--'}`
  },
  [
    {
      name: "FUEL TYPE",
      value: `${FuelType[car.fuel_type] ?? '--'}`
    },
    {
      name: "FUEL AVERAGE DISTANCE",
      value: `${car.fuel_average_distance ?? '--'} km`
    },
    {
      name: "FUEL EFFICIENCY COMBINED",
      value: `${car.fuel_combined ?? '--'}`
    },
    {
      name: "FUEL MINIMUM RANGE",
      value: `${car.min_fuel_distance ?? '--'}`
    },
    {
      name: "FUEL MAXIMUM RANGE",
      value: `${car.max_fuel_distance ?? '--'}`
    },
  ],
  [
    {
      name: "MAXIMUM ELECTRIC RANGE",
      value: `${car.electric_range ?? '--'} km`
    },
    {
      name: "CHARGING TIME 0 - 100% @ 7.4 kWH",
      value: `${convertToTime(car.charging_time)}`
    },
    {
      name: "CHARGING MAXIMUM SPEED",
      value: `${car.fast_charging_max_kw ?? '--'} kW`
    },
  ],
]

const ELECTRIC = [
  [
    {
      name: "POWER (kW/HP) + POWER (rpm)",
      value: `${car.power_kw ?? '--'} kW/${car.power_hp ?? '--'} hp @ ${car.power_rpm ?? '--'} rpm `
    },
    {
      name: "TORQUE + TORQUE Nm",
      value: `${car.torque_nm ?? '--'} Nm @ ${car.torque_rpm ?? '--'} rpm`
    },
    {
      name: "DRIVE",
      value: `${DriveType[car.drive] ?? '--'}`
    },
    {
      name: "ACCELERATION 0 - 100 km/h",
      value: `${car.acceleration ?? '--'} sec`
    },
    {
      name: "TOP SPEED",
      value: `${car.top_speed ?? '--'} km/h`
    }
  ],
  [
    {
      name: "FUEL TYPE",
      value: `${FuelType[car.fuel_type] ?? '--'}`
    },
    {
      name: "MAXIMUM ELECTRIC RANGE",
      value: `${car.electric_range ?? '--'} km`
    },
    {
      name: "CHARGING TIME 0 - 100% @ 7.4 kWH",
      value: `${convertToTime(car.charging_time)}`
    },
    {
      name: "FAST CHARGING",
      value: `FAST CHARGING 10-80% @ 150 kWh - ${convertToTime(car.fast_charging_time)}`
    },
    {
      name: "CHARGING MAXIMUM SPEED - NP. 7.4 kW",
      value: `${car.fast_charging_max_kw ?? '--'} kW`
    },
  ],
]

const PETROL_CAR = [
  [
    {
      name: "ENGINE SIZE",
      value: `${car.engine_size ?? '--'} cm3`
    },
    {
      name: "CYLINDERS &  ENGINE CONFIGURATION",
      value: `${car.cylinders ?? '--'} ${car.engine_configuration ?? '--'} `
    },
    {
      name: "POWER (kW/HP) + POWER (rpm)",
      value: `${car.power_kw ?? '--'} kW/${car.power_hp ?? '--'} hp @ ${car.power_rpm ?? '--'} rpm `
    },
    {
      name: "TORQUE + TORQUE Nm",
      value: `${car.torque_nm ?? '--'} Nm @ ${car.torque_rpm ?? '--'} rpm`
    },
    {
      name: "ACCELERATION 0 - 100 km/h",
      value: `${car.acceleration ?? '--'} sec`
    },
    {
      name: "TOP SPEED",
      value: `${car.top_speed ?? '--'} km/h`
    }
  ],
  [
    {
      name: "DRIVE",
      value: `${DriveType[car.drive] ?? '--'}`
    },
    {
      name: "TRANSMISSION",
      value: `${car.transmission ?? '--'}`
    }],
  {
    name: "GEARS",
    value: `${car.gears ?? '--'}`
  },

  [
    {
      name: "FUEL TYPE",
      value: `${FuelType[car.fuel_type] ?? '--'}`
    },
    {
      name: "FUEL AVERAGE DISTANCE",
      value: `${car.fuel_average_distance ?? '--'} km`
    },
    {
      name: "FUEL EFFICIENCY COMBINED",
      value: `${car.fuel_combined ?? '--'}`
    },
    {
      name: "FUEL MINIMUM RANGE",
      value: `${car.min_fuel_distance ?? '--'}`
    },
    {
      name: "FUEL MAXIMUM RANGE",
      value: `${car.max_fuel_distance ?? '--'}`
    },
  ],
]

const CAR_DETAILS = computed(() => {
  if (car.fuel_type === FuelTypeEnum.ELECTRIC) return ELECTRIC
  if (car.fuel_type === FuelTypeEnum.PHEV) return PHEV
  return PETROL_CAR
})


</script>

<style scoped>
.details-box {
  padding: 20px 40px;
  margin-top: 10px;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
  height: 400px;
  overflow-y: auto;
}

.details-box ul {
  list-style: none;
  padding-left: 0;
}

.details-box ul li {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  padding-bottom: 7px;
}

.details-box ul li .name {
  font-weight: 900;
  text-align: left;
  width: 60%;
}

.details-box ul li .value {
  font-weight: 700;
  text-align: left;
  width: 40%;
}
</style>