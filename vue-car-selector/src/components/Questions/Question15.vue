<template>
  <div>
    <question-label
        number="15"
        help-text="The more specific you can be - the better the match. But feel free to skip if you aren’t quite sure!"
        question="Which feature(s) are important to you?"/>
    <div class="answers-box">

      <div class="section-text">GENERAL</div>
      <checkout-field v-model="question.comfort" label="comfort"/>
      <checkout-field v-model="question.overall_style" label="overall style"/>
      <checkout-field v-model="question.min_5_years_warranty" label="minimum 5 years warranty"/>
      <checkout-field v-model="question.highest_safety_ratings" label="highest safety ratings"/>
      <checkout-field v-model="question.low_fuel_economy" label="low fuel economy"/>

      <div class="section-text">CABIN</div>
      <checkout-field v-model="question.practicality_cabin" label="practicality - cabin & space"/>
      <checkout-field v-model="question.premium_cabin" label="premium cabin"/>
      <checkout-field v-model="question.folding_back_seats" label="folding back seats"/>
      <checkout-field v-model="question.high_tech_info_system" label="high-tech infotainment system"/>

      <!--      <div class="section-text">SAFETY</div>-->
      <!--      <checkout-field v-model="question.adult_safe" label="keeping adults safe"/>-->
      <!--      <checkout-field v-model="question.children_safe" label="keeping children safe"/>-->
      <!--      <checkout-field v-model="question.other_road_users_safe" label="keeping other road users safe"/>-->
      <!--      <checkout-field v-model="question.assistance_system" label="having the safest assistance systems"/>-->


      <div class="section-text">SPORTINESS</div>
      <checkout-field v-model="question.sport_feel" label="sporty feel"/>
      <checkout-field v-model="question.handling_dynamics" label="handling dynamics"/>
      <checkout-field v-model="question.race_track" label="I want a sports car"/>
      <checkout-field v-model="question.race_track_plus" label="I want to take my car to a racetrack"/>

      <div class="section-text">VARIOUS</div>
      <checkout-field v-model="question.light_off_road" label="occasional light off-road"/>
      <checkout-field v-model="question.heavy_off_road" label="heavy off-road"/>
      <checkout-field v-model="question.tall_driver" label="tall driver - over 1.9 m"/>
      <checkout-field v-model="question.first_time_drive" label="new driver"/>
      <checkout-field v-model="question.rapid_charging" label="rapid charging - over 200 kWh (electric cars)"/>

      <div class="section-text" style="margin-top: 30px">HOW EFFICIENT?</div>
      <div class="section-subtext">RANGE (km) - including ELECTRIC cars</div>
      <div class="slider">
        <span>0 km</span>
        <Slider :min="0"
                :step="10"
                :max="MAX_RANGE_KM"
                class="range-km"
                :format="{
                  suffix: 'km'
                }"
                :merge="200"
                connects='c-slider-connects'
                v-model="range_km.value"
                v-bind="range_km"/>
        <span>{{ MAX_RANGE_KM }} km</span>
      </div>

      <div class="section-subtext">FUEL ECONOMY (L/100km)</div>
      <div class="slider">
        <span>0 L</span>
        <Slider :min="0"
                :max="MAX_FUEL_ECONOMY"
                :format="{
                  suffix: ' L'
                }"
                :merge="2"
                class="fuel-economy"
                connects='c-slider-connects'
                v-model="fuel_economy.value"
                v-bind="fuel_economy"/>
        <span>{{ MAX_FUEL_ECONOMY }} L</span>
      </div>

      <div class="section-text" style="margin-top: 30px">LET’S TALK NUMBERS</div>
      <div class="section-subtext">POWER - minimum kW</div>
      <div class="slider">
        <span>0 kW</span>
        <Slider :min="0"
                :max="MAX_POWER_KW"
                :step="10"
                class="power-kw"
                :format="hp_label_computed"
                connects='c-slider-connects'
                v-model="question.power__gte"/>
        <span>{{ MAX_POWER_KW }} kW</span>
      </div>


      <div class="section-subtext">ACCELERATION 0-100 km/h - maximum seconds</div>
      <div class="slider">
        <span>0 sec</span>
        <Slider :min="0"
                :max="MAX_ACCELERATE"
                :format="{
                  suffix: ' sec'
                }"
                class="acceleration"
                connects='c-slider-connects'
                v-model="question.acceleration__lte"/>
        <span>{{ MAX_ACCELERATE }} sec</span>
      </div>
      <div class="section-subtext">ENGINE SIZE - L - minimum volume</div>
      <div class="slider">
        <span>0 L</span>
        <Slider :min="0"
                :max="MAX_ENGINE_SIZE"
                class="engine"
                :format="{
                  suffix: ' L'
                }"
                connects='c-slider-connects'
                v-model="question.engine__gte"/>
        <span>{{ MAX_ENGINE_SIZE }} L</span>
      </div>
    </div>
    <div>

    </div>
  </div>
</template>

<script setup>
import {computed, reactive, ref, watch} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckboxField";
import Slider from '@vueform/slider'


const MAX_RANGE_KM = 2200;
const MAX_FUEL_ECONOMY = 25;
const MAX_ENGINE_SIZE = 7;
const MAX_ACCELERATE = 20;
const MAX_POWER_KW = 600;
const emit = defineEmits(['answers'])

const range_km = reactive({
  value: [0, MAX_RANGE_KM]
})
const fuel_economy = reactive({
  value: [0, MAX_FUEL_ECONOMY]
})
const question = reactive({
  comfort: null,
  overall_style: null,
  min_5_years_warranty: null,
  highest_safety_ratings: null,
  low_fuel_economy: null,

  practicality_cabin: null,
  premium_cabin: null,
  folding_back_seats: null,
  high_tech_info_system: null,
  adult_safe: null,
  children_safe: null,
  other_road_users_safe: null,
  assistance_system: null,
  km_range__gte: null,
  km_range__lte: null,
  fuel_economy__gte: null,
  fuel_economy__lte: null,
  power__gte: null,
  acceleration__lte: null,
  engine__gte: null,
  sport_feel: null,
  handling_dynamics: null,
  race_track: null,
  race_track_plus: null,
  rapid_charging: null,
  light_off_road: null,
  heavy_off_road: null,
  tall_driver: null,
  first_time_drive: null,

})
const hp_label_computed = ref({
  suffix: ' kW',
  decimals: 0
})


watch(() => question.acceleration__lte, () => {
  if (question.acceleration__lte === 0 || question.acceleration__lte === MAX_ACCELERATE) {
    question.acceleration__lte = null;
  }
})

watch(() => question.power__gte, () => {
  if (question.power__gte === 0) {
    question.power__gte = null;
  }
})

watch(() => question.engine__gte, () => {
  if (question.engine__gte === 0) {
    question.engine__gte = null;
  }
})

watch(range_km, () => {
  range_km.value[1] !== MAX_RANGE_KM ? question.km_range__lte = range_km.value[1] : question.km_range__lte = null;
  range_km.value[0] ? question.km_range__gte = range_km.value[0] : question.km_range__gte = null;
})

watch(fuel_economy, () => {
  fuel_economy.value[1] !== MAX_FUEL_ECONOMY ? question.fuel_economy__lte = fuel_economy.value[1] : question.fuel_economy__lte = null;
  fuel_economy.value[0] ? question.fuel_economy__gte = fuel_economy.value[0] : question.fuel_economy__gte = null;
})


watch(question, () => {
  emitData();
})


const emitData = () => {
  emit('answers', {
        comfort: question.comfort,
        overallStyle: question.overall_style,
        min5YearsWarranty: question.min_5_years_warranty,
        highestSafetyRatings: question.highest_safety_ratings,
        lowFuelEconomy: question.low_fuel_economy,
        practicalityCabin: question.practicality_cabin,
        premiumCabin: question.premium_cabin,
        foldingBackSeats: question.folding_back_seats,
        highTechInfoSystem: question.high_tech_info_system,
        adultSafe: question.adult_safe,
        childrenSafe: question.children_safe,
        otherRoadUsersSafe: question.other_road_users_safe,
        assistanceSystem: question.assistance_system,
        sportFeel: question.sport_feel,
        handlingDynamics: question.handling_dynamics,
        raceTrack: question.race_track,
        kmRangeGte: question.km_range__gte,
        kmRangeLte: question.km_range__lte,
        fuelEconomyGte: question.fuel_economy__gte,
        fuelEconomyLte: question.fuel_economy__lte,
        powerGte: question.power__gte,
        accelerationLte: question.acceleration__lte,
        engineGte: question.engine__gte,
        raceTrackPlus: question.race_track_plus,
        rapidCharging: question.rapid_charging,
        lightOffRoad: question.light_off_road,
        heavyOffRoad: question.heavy_off_road,
        tallDriver: question.tall_driver,
        firstTimeDrive: question.first_time_drive,
      }
  )
}
</script>
<style>
.slider-horizontal .slider-tooltip-top {
  bottom: 15px !important;
}
</style>
<style scoped>

.slider div {
  width: 100%;
}

.slider span:last-child,
.slider span:first-child {
  position: absolute;
  top: 15px;
  background-color: transparent !important;
  box-shadow: none !important;
  font-size: 12px !important;
  font-weight: 800 !important;
}

.slider span:first-child {
  left: -10px;
}

.slider span:last-child {
  right: -10px;
}

.slider {
  position: relative;
  display: flex;
  width: 100%;
  margin-bottom: 40px;
  margin-top: 20px;
}

</style>
<style src="@vueform/slider/themes/default.css"></style>