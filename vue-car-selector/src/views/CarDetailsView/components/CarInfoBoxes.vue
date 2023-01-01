<template>
  <div class="top-container" style="margin-top: 40px;">
    <div class="top">
      <div> ${{ Formatter.formatPrice(car.price_au) }}</div>
      <span class="section-text-subtitle">price</span>
    </div>
    <div class="top">
      <div> {{ car.acceleration ? parseFloat(car.acceleration).toFixed(1) : '--' }}SEC</div>
      <span class="section-text-subtitle">acceleration</span>
    </div>
    <div class="top">
      <div> {{ car.top_speed }}KM/H</div>
      <span class="section-text-subtitle">top speed</span>
    </div>
  </div>
  <div class="top-container">
    <div class="top-bottom">
      <div> ${{ Formatter.formatPrice(car.price_au) }}</div>
      <span class="section-text-subtitle">price</span>
    </div>
    <div class="top-bottom">
      <div> {{ car.acceleration ? parseFloat(car.acceleration).toFixed(1) : '--' }}SEC</div>
      <span class="section-text-subtitle">acceleration</span>
    </div>
    <div class="top-bottom">
      <div> {{ car.top_speed }}KM/H</div>
      <span class="section-text-subtitle">top speed</span>
    </div>
  </div>
</template>

<script setup>
import {computed, defineProps} from "vue";
import {DriveType, FuelType, FuelTypeEnum} from "../../../dicts";
import {Formatter} from "../../../utils";

const props = defineProps(['car']);
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
  padding: 15px 0;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
  font-weight: 600;
  font-size: 23px;
  border: 3px solid rgba(196, 44, 140, 0.76);
  border-top: none;

span {
  text-transform: uppercase;
  display: block;
  font-size: 12px;
}

}

.top:first-child {
  border-left: 6px solid rgba(196, 44, 140, 0.76);
}

.top:last-child {
  border-right: 6px solid rgba(196, 44, 140, 0.76);;
}

.top-bottom {
  border: 4px solid rgba(196, 44, 140, 0.76);
  border-bottom: none;
}

.top-bottom:first-child {
  border-left: none;
}

.top-bottom:last-child {
  border-right: none;
}
</style>