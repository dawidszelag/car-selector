<template>
  <div>
    <div class="car-name">
      <span> {{ car.model.brand.name }}</span> {{ car.model.name }}
      <div>{{ car.name }}</div>
    </div>
    <div class="section-text-d" style="margin-top: 40px;">
      TOP
    </div>
    <div class="top-container">
      <div class="top">
        <div> {{ car.acceleration ? parseFloat(car.acceleration).toFixed(1) : '--' }}SEC <span>acceleration</span></div>
      </div>
      <div class="top">
        <div> {{ car.top_speed }}KM/H <span>top speed</span></div>
      </div>
      <div class="top">
        <div> ${{ formatPrice(car.price_au) }} <span>price</span></div>
      </div>
    </div>
    <div class="section-text-d" style="margin-top: 40px;">
      DETAILS
    </div>
    <div class="details">
      <div class="details-line">
        <div>{{ DriveType[car.drive] }}</div>
        <div>{{ car.gears }} GEARS</div>
        <div>{{ car.seats }} SEATS</div>
        <div>{{ car.doors }} DOORS</div>
      </div>
      <div class="details-box">
        <ul>
          <li>
            <div class="name">NAMING</div>
            <div class="value">{{ car.name }}</div>
          </li>
          <li>
            <div class="name">PRICE</div>
            <div class="value">${{ formatPrice(car.price_au) }}</div>
          </li>
        </ul>
        <ul>
          <li>
            <div class="name">BODY</div>
            <div class="value">{{ car.body.name }}</div>
          </li>
          <li>
            <div class="name">DOORS</div>
            <div class="value">{{ car.doors }}</div>
          </li>
          <li>
            <div class="name">SEATS</div>
            <div class="value">{{ car.seats }}</div>
          </li>


        </ul>
        <ul>
          <li>
            <div class="name">LENGTH</div>
            <div class="value">{{ car.length }}</div>
          </li>
          <li>
            <div class="name">WIDTH</div>
            <div class="value">{{ car.width }}</div>
          </li>
          <li>
            <div class="name">HEIGHT</div>
            <div class="value">{{ car.height }}</div>
          </li>
          <li>
            <div class="name">WHEEL BASE</div>
            <div class="value">{{ car.wheelbase }}</div>
          </li>
          <li>
            <div class="name">TARE MASS (KG)</div>
            <div class="value">{{ car.tare_mass }}</div>
          </li>
          <li>
            <div class="name">GROUND CLEARANCE</div>
            <div class="value">{{ car.ground_clearance }}</div>
          </li>
        </ul>
        <ul>
          <li>
            <div class="name">MINIMUM BOOT SPACE</div>
            <div class="value">{{ car.min_boot_space }}</div>
          </li>
          <li>
            <div class="name">MAXIMUM BOOT SPACE</div>
            <div class="value">{{ car.max_boot_space }}</div>
          </li>
          <li>
            <div class="name">FOLDABLE BACK SEATS - YES/NO</div>
            <div class="value"><span v-if=" car.foldable_seats">YES</span><span v-else>NO</span></div>
          </li>

        </ul>
        <ul>
          <li>
            <div class="name">TRANSMISSION</div>
            <div class="value">{{ car.transmission }}</div>
          </li>
          <li>
            <div class="name">GEARS</div>
            <div class="value">{{ car.gears }}</div>
          </li>
          <li>
            <div class="name">DRIVE</div>
            <div class="value">{{ DriveType[car.drive] }}</div>
          </li>

        </ul>
        <ul>
          <li>
            <div class="name">ENGINE LOCATION</div>
            <div class="value">{{ car.engine_location }}</div>
          </li>
          <li>
            <div class="name">ENGINE SIZE</div>
            <div class="value">{{ car.engine_size }}cm3</div>
          </li>
          <li>
            <div class="name">ENGINE CONFIGURATION</div>
            <div class="value">{{ car.engine_configuration }}</div>
          </li>
          <li>
            <div class="name">CYLINDERS</div>
            <div class="value">{{ car.cylinders }}</div>
          </li>
          <li>
            <div class="name">POWER HP</div>
            <div class="value">{{ car.power_kw }}</div>
          </li>
          <li>
            <div class="name">POWER kW</div>
            <div class="value">{{ car.power_hp }}</div>
          </li>
          <li>
            <div class="name">POWER rpm</div>
            <div class="value">{{ car.power_rpm }}</div>
          </li>
          <li>
            <div class="name">TORQUE</div>
            <div class="value">{{ car.torque_nm }}</div>
          </li>
          <li>
            <div class="name">TORQUE RPM</div>
            <div class="value">{{ car.torque_rpm }}</div>
          </li>
          <li>
            <div class="name">ACCELERATION 0-100 (SEC)</div>
            <div class="value">{{ car.acceleration }}</div>
          </li>
          <li>
            <div class="name">TOP SPEED (KM/H)</div>
            <div class="value">{{ car.top_speed }}</div>
          </li>

        </ul>
        <ul>
          <li>
            <div class="name">FUEL TYPE</div>
            <div class="value">{{ FuelType[car.fuel_type] }}</div>
          </li>
          <li>
            <div class="name">FUEL CAPACITY</div>
            <div class="value">{{ car.fuel_capacity }}</div>
          </li>
          <li>
            <div class="name">FUEL COMBINED</div>
            <div class="value">{{ car.fuel_combined }}</div>
          </li>
          <li>
            <div class="name">FUEL URBAN</div>
            <div class="value">{{ car.fuel_urban }}</div>
          </li>
          <li>
            <div class="name">FUEL AVERAGE DISTANCE (KM)</div>
            <div class="value">{{ car.fuel_average_distance }}</div>
          </li>
          <li v-if="car.electric_range">
            <div class="name">ELECTRIC RANGE (KM)</div>
            <div class="value">{{ car.electric_range }}</div>
          </li>

        </ul>
        <ul>
          <li>
            <div class="name">ANCAP RATING - OUT OF 5*</div>
            <div class="value">{{ car.ancap }}</div>
          </li>
          <li>
            <div class="name">WARRANTY (YEARS)</div>
            <div class="value">{{ car.warranty_years }}</div>
          </li>
          <li>
            <div class="name">WARRANTY (KM)</div>
            <div class="value">{{ car.warranty_distance }}</div>
          </li>
          <li v-if="parseInt(car.battery_warranty_years)">
            <div class="name">BATTERY WARRANTY (YEARS)</div>
            <div class="value">{{ car.battery_warranty_years }}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {defineProps} from "vue";
import {DriveType, FuelType} from "../dicts";

defineProps(['car']);

const formatPrice = (value) => {
  let val = (value / 1).toFixed(0).replace('.', ',')
  return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
}
</script>
<style lang="less" scoped>

.details-box {
  padding:  20px 40px;
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
  text-align: right;
}

.details-box ul li .value {
  font-weight: 700;
  text-align: right;
}

.top-container {
  display: flex;
  justify-content: space-between;
}

.details-line {
  position: relative;
  text-transform: uppercase;
  display: flex;
  justify-content: space-between;
  padding: 5px 20px;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
  font-weight: 900;
  font-size: 12px;

  &:before {
    position: absolute;
    left: -8px;
    top: 0;
    content: "";
    width: 5px;
    height: 100%;
    background: linear-gradient(#d71d80, #c42c8c) rgba(176, 30, 30, 0.3);
    box-shadow: 0 3px 4px rgba(0, 0, 0, 0.4);
  }
}


.top {
  width: 30%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  padding: 15px 0;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
  font-weight: 600;
  font-size: 23px;

  span {
    text-transform: uppercase;
    display: block;
    font-size: 12px;
  }
}

.top:before {
  position: absolute;
  left: -8px;
  top: 0;
  content: "";
  width: 5px;
  height: 100%;
  background: linear-gradient(#d71d80, #c42c8c) rgba(176, 30, 30, 0.3);
  box-shadow: 0 3px 4px rgba(0, 0, 0, 0.4);
}

.car-name {
  font-size: 40px;
  font-weight: 700;

  span {
    color: rgb(215, 29, 128);
  }

  div {
    font-size: 20px;
    font-weight: 600;
  }
}

</style>