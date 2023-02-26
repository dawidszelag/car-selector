<template>
  <div style="position: relative">
    <div class="brand" v-if="brandThumbnail">
      <div>
        <img :src="brandThumbnail" alt="">
      </div>
    </div>
    <div class="car-name">
      <span> {{ car.model.brand.name }}</span> {{ car.model.name }}
      <div>{{ car.name }}</div>
    </div>
    <CarInfoBoxes :car="car"/>
    <CarStats :car="car"/>
    <CarDetails :car="car"/>
  </div>
</template>

<script setup lang="ts">
import {computed, defineProps, onBeforeMount, ref} from "vue";
import CarDetails from "./CarDetials.vue";
import CarInfoBoxes from "./CarInfoBoxes.vue";
import {CarBrandOut, CarsService} from "../../../api";
import CarStats from "./CarStats.vue";

const props = defineProps(['car']);
const {car} = props;
const brands = ref<CarBrandOut[]>([])
onBeforeMount(async () => {
  brands.value = await CarsService.getBrands();
})

const brandThumbnail = computed(() => {
  return brands.value.find(item => item.id === car.model.brand.id)?.thumbnail
})

</script>
<style lang="less" scoped>
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


.car-name {
  text-transform: uppercase;
  font-size: 40px;
  font-weight: 700;

  span {
    color: rgb(215, 29, 128);
  }

  div {
    text-transform: none;
    font-size: 20px;
    font-weight: 600;
  }
}

.brand {
  max-width: 100px;
  position: absolute;
  text-align: left;
  right: 100px;

  img {
    width: 100%;
  }
}


</style>