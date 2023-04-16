<template>
  <div class="container"
       :style="{ backgroundImage: 'url(' +  carBGImage  + ')' }"
       style="background-position: center; background-size: cover;">
    <div class="content">
      <SendFeedback v-model:visible="showModal" @ready="router.push({name: 'home'})"/>
      <CarInfo v-if="car" :car="car" class="box"/>
      <div class="box" v-if="car">
        <CarMatch style="min-height: 300px; margin-bottom: 50px;" :car="car"/>
        <CarGallery :images="car.images">
          <div class="footer">
            <div class="nav-button-right" @click="handleBackToList">
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
import {useRoute, useRouter} from "vue-router"
import {CarsService} from "../../api";
import CarGallery from "../../components/CarGallery";
import SendFeedback from "../../components/SendFeedback";
import CarInfo from "./components/CarInfo.vue";
import CarMatch from "./components/CarMatch.vue";
import {useAppStore} from "../../store";
const router = useRouter()
const car = ref<CarDetailsOut | null>(null);
const route = useRoute();
const appStore =  useAppStore()
const showModal = ref(false)
onBeforeMount(async () => {
  car.value = await CarsService.getCarDetails({carId: route.params.carId as number})
})

const carBGImage = computed(() => {
  return car.value?.images?.length ? OpenAPI.BASE + car.value.images[0].image : bgImage
})

const handleBackToList = ()=>{
  if (!appStore.showFeedBack){

    appStore.setFeedback();
    showModal.value = true;
  }
  else{
    router.push({name: 'home'})
  }
}
</script>

<style scoped lang="less">

.container .content {
  display: flex;
  width: 100%;
  min-height: 100vh;
  position: relative;
  .box {
    width: 50%;
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
    padding: 100px 5%;
    background: rgba(36, 36, 36, 0.9);

    &:nth-child(2) {
      background: rgba(36, 36, 36, 0.8);
    }
  }

}

</style>