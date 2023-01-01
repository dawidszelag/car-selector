<template>
  <div class="container"
       :style="{ backgroundImage: 'url(' +  carBGImage  + ')' }"
       style="background-position: center; background-size: cover;">
    <CarInfo v-if="car" :car="car" class="box"/>
    <div class="box" v-if="car">
      <CarGallery :images="car.images"/>
      <div>
        <div class="section-text-d" style="margin-top: 20px">
          CARMATCH #
        </div>
        <div class="carmatch">
          <div class="badge" v-if="car?.anna_cars">
            <img :src="BagdeAnnaChoice" alt="">
          </div>
        </div>
      </div>
    </div>
    <div class="nav-right" @click="$router.push({name: 'home'})">
      BACK TO LIST
    </div>
  </div>
</template>

<script setup>
import bgImage from "@/assets/bg-pc.jpg"
import {OpenAPI} from '../../api';
import BagdeAnnaChoice from "@/assets/badge-1.png"
import {computed, onBeforeMount, ref} from "vue";
import {useRoute} from "vue-router"
import {CarsService} from "../../api";
import CarGallery from "../../components/CarGallery";
import CarInfo from "./components/CarInfo";

const car = ref(null);
const route = useRoute();

onBeforeMount(async () => {
  car.value = await CarsService.getCarDetails({carId: route.params.carId})
})

const carBGImage = computed(() => {
  return car.value?.images.length ? OpenAPI.BASE + car.value.images[0].image : bgImage
})
</script>

<style scoped lang="less">
.carmatch {
  display: flex;

  .badge img {
    max-width: 80px;
  }
}

.container {
  display: flex;
  width: 100%;
  min-height: 100vh;

  .box {
    width: 50%;
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
    padding: 100px 5%;

    &:nth-child(2) {
      background: rgba(36, 36, 36, 0.3);
    }
  }

}

</style>