<template>
  <div class="questions">
    <Modal class="modal" v-model:visible="showModalElectric">
      For short distances and local driving, diesel is not recommended. Instead, we suggest the following:
      <ul>
        <li> petrol </li>
        <li>hybrid petrol - HEV</li>
        <li>plug-in hybrid petrol - PHEVmild hybrid petrol - MHEV</li>
        <li>electric</li>
      </ul>
    </Modal>
    <Modal class="modal" v-model:visible="showModalDiesel">
      For long distances, an electric car is not recommended. Instead, we suggest the following:
      <ul>
        <li>petrol</li>
        <li>diesel</li>
        <li>hybrid petrol - HEV</li>
        <li>plug-in hybrid petrol - PHEV</li>
        <li>mild hybrid petrol - MHEV</li>
        <li>mild hybrid diesel - MHEV</li>
      </ul>
    </Modal>
    <Modal class="modal" v-model:visible="showModal">
      <div>This selection is non-compatible with your other answers. Try another response.</div>
    </Modal>
    <div class="section-title">
      LET'S <span>GET</span> STARTED
    </div>
    <question1 @answers="handleAnswers" class="question"/>
    <question2 @answers="handleAnswers" class="question"/>
    <question3 @answers="handleAnswers" class="question"/>
    <question4 v-if="budget" @answers="handleAnswers" class="question" :minValue="budget.min" :maxValue="budget.max"/>
    <question5 @answers="handleAnswers" class="question" :brands="brands"/>
    <question6 @answers="handleAnswers" class="question" :bodies="bodies"/>
    <question7 @answers="handleAnswers" class="question"/>
    <question8 @answers="handleAnswers" class="question"/>
    <question9 @answers="handleAnswers" class="question"/>
    <question10 @answers="handleAnswers" class="question"/>
    <question11 @answers="handleAnswers" class="question"/>
    <question12 @answers="handleAnswers" class="question"/>
    <question13 @answers="handleAnswers" class="question"/>
    <question14 @answers="handleAnswers" class="question"/>
    <question15 @answers="handleAnswers" class="question"/>
    <question16 class="question"/>
    <div class="carCounter" v-if="!buttonIsVisible">
      MATCHING CARS: {{ countCars }}
    </div>
    <div class="button-container" v-intersection-observer="onIntersectionObserver">
      <button class="show-car-button" :disabled="!countCars" @click="$emit('ready', form)">
        <span v-if="countCars"> VIEW YOUR ({{ countCars }}) MATCHES</span>
        <span v-else>NO MATCHES</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import {vIntersectionObserver} from '@vueuse/components'
import Question1 from "../components/Questions/Question1";
import Question2 from "../components/Questions/Question2";
import {onBeforeMount, reactive, ref, watch} from "vue";
import Question3 from "../components/Questions/Question3";
import Question4 from "../components/Questions/Question4";
import Question5 from "../components/Questions/Question5";
import Question6 from "../components/Questions/Question6";
import {CarsService} from "../api";
import Question7 from "../components/Questions/Question7";
import Question8 from "../components/Questions/Question8";
import Question9 from "../components/Questions/Question9";
import Question10 from "../components/Questions/Question10";
import Question11 from "../components/Questions/Question11";
import Question12 from "../components/Questions/Question12";
import Question13 from "../components/Questions/Question13";
import Question14 from "../components/Questions/Question14";
import Question15 from "../components/Questions/Question15";
import Question16 from "../components/Questions/Question16";
import {Modal} from 'usemodal-vue3';

const showModal = ref(false)
const showModalDiesel = ref(false)
const showModalElectric = ref(false)
const buttonIsVisible = ref(false)
const brands = ref([]);
const bodies = ref([]);
const budget = ref(null);
const isReady = ref(false);
const countCars = ref(0)
const form = reactive({
  annaForWomen: null,

  youngDriver: null,
  driver2345: null,
  middleAgedDriver: null,
  olderDriver: null,

  shortDistance: null,
  longDistance: null,
  mixedDistance: null,
  perfectCityCar: null,

  priceAuGte: null,
  priceAuLte: null,
  priceNzGte: null,
  priceNzLte: null,

  brandsIdIn: null,
  bodiesIdIn: null,

  compact: null,
  medium: null,
  large: null,

  petrol: null,
  diesel: null,
  hev: null,
  phev: null,
  mhevPetrol: null,
  mhevDiesel: null,
  electric: null,

  twoDoors: null,
  fourDoors: null,

  seats: null,

  flexible: null,
  elderlyFrontSeat: null,
  children: null,
  regularlyPlusOneAdult: null,
  threeAdultsBackSeat: null,
  elderlyBackSeat: null,
  dogs: null,

  bootLte: null,
  bootGte: null,
  bootUte: null,

  fwd: null,
  rwd: null,
  awd: null,

  automatic: null,
  manual: null,


  comfort: null,
  overallStyle: null,
  min5YearsWarranty: null,
  practicalityCabin: null,
  premiumCabin: null,
  foldingBackSeats: null,
  highTechInfoSystem: null,
  adultSafe: null,
  childrenSafe: null,
  otherRoadUsersSafe: null,
  assistanceSystem: null,
  sportFeel: null,
  handlingDynamics: null,
  raceTrack: null,
  kmRangeGte: null,
  kmRangeLte: null,
  fuelEconomyGte: null,
  fuelEconomyLte: null,
  powerGte: null,
  powerLte: null,
  accelerationGte: null,
  accelerationLte: null,
  engineGte: null,
  engineLte: null,

})

function onIntersectionObserver([{isIntersecting}]) {
  buttonIsVisible.value = isIntersecting
}

const handleAnswers = (data) => {
  Object.assign(form, data)
  makeRequest();
}


const makeRequest = async () => {
  const response = await CarsService.getCars(form);
  countCars.value = response.count;
  if (response.count === 0 && !showModalDiesel.value && !showModalElectric) {
    showModal.value = true;
  }
}

onBeforeMount(async () => {
      brands.value = await CarsService.getBrands();
      bodies.value = await CarsService.getBodies();
      budget.value = await CarsService.getBudget();
      await makeRequest();
      isReady.value = true;
    }
)

watch(() => form.diesel, () => {
  if (form.shortDistance && form.diesel) {
    showModalDiesel.value = true;
  }
})

watch(() => form.electric, () => {
  if (form.longDistance && form.electric) {
    showModalDiesel.value = true;
  }
})
</script>
<style lang="less">

</style>
<style scoped lang="less">


.questions {
  position: relative;
}

.question:first-child {
  margin-top: 0;
}

.question {
  margin-top: 50px;
}

.button-container {
  display: flex;
  justify-content: center;
}

.show-car-button {
  cursor: pointer;
  padding: 20px 40px;
  font-weight: 900;
  margin: 40px 0;
  color: white;
  font-size: 15px;
  outline: rgba(0, 0, 0, 0.2) 3px solid;
  border: none;
  background: linear-gradient(rgba(215, 29, 128, 1), rgba(196, 44, 140, 1)) !important;
}

.show-car-button:disabled {
  background: linear-gradient(rgba(215, 29, 128, 0.5), rgba(196, 44, 140, 0.5)) !important;
}

.carCounter {
  position: fixed;
  z-index: 100;
  bottom: 0;
  right: 5px;
  padding: 10px 20px;
  font-weight: 900;
  font-size: 14px;
  background: linear-gradient(rgba(215, 29, 128, 1), rgba(196, 44, 140, 1)) !important;
}

.section-title {
  font-style: italic;
  font-size: 30px;
  font-weight: 800;
  margin-left: -10px;

  span {
    color: rgb(215, 29, 128);
  }
}

:deep(.modal-vue3-header) {
  display: none;
}

:deep(.modal-vue3-content) {
  border: none !important;
  color: rgba(255, 255, 255, 0.85) !important;
  background: rgba(36, 36, 36, 0.85) !important;
  box-shadow: 0 2px 3px rgb(0 0 0 / 40%) !important;
}

:deep(.modal-vue3-footer) {
  border-top: none !important;
}

:deep(.modal-vue3-footer-cancel) {
  display: none !important;
}

:deep(.modal-vue3-footer-ok) {
  background: linear-gradient(rgba(215, 29, 128, 0.9), rgba(196, 44, 140, 0.9)) !important;
}
</style>