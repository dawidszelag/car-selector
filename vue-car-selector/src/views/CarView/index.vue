<template>
  <div class="container"
       :style="{ backgroundImage: 'url(' +  carBGImage  + ')' }"
       style="background-position: center; background-size: cover;">
    <div class="content">
      <CarInfo v-if="car" :car="car" class="box"/>
      <div class="box" v-if="car">
        <CarMatch style="min-height: 300px; margin-bottom: 100px;" :car="car"/>
        <CarGallery style="max-height: 400px;">
          <div class="footer">
            <div class="nav-button-right" @click="$router.push({name: 'home'})">
              BACK TO LIST
            </div>
          </div>
        </CarGallery>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import bgImage from "@/assets/bg-pc.jpg"
import {CarDetailsOut, OpenAPI} from '../../api';

import {computed, onBeforeMount, ref} from "vue";
import {useRoute} from "vue-router"
import {CarsService} from "../../api";
import CarGallery from "../../components/CarGallery";
import CarInfo from "./components/CarInfo.vue";
import CarMatch from "./components/CarMatch.vue";

const car = ref<CarDetailsOut | null>(null);
const route = useRoute();

onBeforeMount(async () => {
  car.value = await CarsService.getCarDetails({carId: route.params.carId as number})
})

const carBGImage = computed(() => {
  return car.value?.images?.length ? OpenAPI.BASE + car.value.images[0].image : bgImage
})
</script>

<style scoped lang="less">

.container .content {
  display: flex;
  width: 100%;
  height: 100vh;

  .box {
    width: 50%;
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
    padding: 100px 5%;
    background: rgba(36, 36, 36, 0.8);

    &:nth-child(2) {
      background: rgba(36, 36, 36, 0.6);
    }
  }

}

</style>