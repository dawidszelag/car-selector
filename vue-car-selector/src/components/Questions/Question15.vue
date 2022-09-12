<template>
  <div>
    <question-label
        number="15"
        help-text="- select all that apply"
        question="Which feature are important to you?"/>
    <div class="answers-box">

      <div class="section-text">GENERAL:</div>
      <checkout-field v-model="question.comfort" label="comfort"/>
      <checkout-field v-model="question.overall_style" label="overall style"/>
      <checkout-field v-model="question.min_5_years_warranty" label="minimum 5 years warranty"/>

      <div class="section-text">CABIN:</div>
      <checkout-field v-model="question.practicality_cabin" label="practicality - cabin & space"/>
      <checkout-field v-model="question.premium_cabin" label="premium cabin"/>
      <checkout-field v-model="question.folding_back_seats" label="folding back seats"/>
      <checkout-field v-model="question.high_tech_info_system" label="high-tech infotainment system"/>

      <div class="section-text">SAFETY:</div>
      <checkout-field v-model="question.adult_safe" label="keeping adults safe"/>
      <checkout-field v-model="question.children_safe" label="keeping children safe"/>
      <checkout-field v-model="question.other_road_users_safe" label="keeping other road users safe"/>
      <checkout-field v-model="question.assistance_system" label="having the safest assistance systems"/>


      <div class="section-text">SPORTINESS:</div>
      <checkout-field v-model="question.sport_feel" label="sporty feel"/>
      <checkout-field v-model="question.handling_dynamics" label="handling dynamics"/>
      <checkout-field v-model="question.race_track" label="I want to take my car to a racetrack"/>

      <div class="section-text" style="margin-top: 30px">How efficient should your car be?</div>
      <div class="section-subtext">RANGE (km)</div>
      <MultiRangeSlider
          class="range-km"
          style="max-width: 535px"
          :min="0"
          :max="1200"
          :step="10"
          :ruler="false"
          :label="false"
          :minValue="0"
          :maxValue="1200"
          @input="rangeHandler"
      />

      <div class="section-subtext">FUEL ECONOMY (L/100km)</div>
      <MultiRangeSlider
          class="fuel-economy"
          style="max-width: 535px"
          :min="0"
          :max="25"
          :step="1"
          :ruler="false"
          :label="false"
          :minValue="0"
          :maxValue="25"
          @input="fuelEconomyHandler"
      />

      <div class="section-text" style="margin-top: 30px">Let's talk numbers?</div>
      <div class="section-subtext">Power (kW)</div>
      <MultiRangeSlider
          class="power-kw"
          style="max-width: 535px"
          :min="0"
          :max="1000"
          :step="10"
          :ruler="false"
          :label="false"
          :minValue="0"
          :maxValue="1000"
          @input="powerHandler"
      />

      <div class="section-subtext">Acceleration 0-100 km/h (seconds)</div>
      <MultiRangeSlider
          class="acceleration"
          style="max-width: 535px"
          :min="0"
          :max="20"
          :step="1"
          :ruler="false"
          :label="false"
          :minValue="0"
          :maxValue="20"
          @input="accelerationHandler"
      />

      <div class="section-subtext">Engine size (L)</div>
      <MultiRangeSlider
          class="engine"
          style="max-width: 535px"
          :min="0"
          :max="9"
          :step="0.5"
          :ruler="false"
          :label="false"
          :minValue="0"
          :maxValue="9"
          @input="engineHandler"
      />

    </div>
    <div>

    </div>
  </div>
</template>

<script setup>
import {reactive, watch} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckoutField";
import MultiRangeSlider from "multi-range-slider-vue";

const emit = defineEmits(['answers'])
const question = reactive({
  comfort: null,
  overall_style: null,
  min_5_years_warranty: null,
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
  power__lte: null,
  acceleration__gte: null,
  acceleration__lte: null,
  engine__gte: null,
  engine__lte: null,
  sport_feel: null,
  handling_dynamics: null,
  race_track: null,

})
const rangeHandler = (e) => {
  e.minValue !== 0 ? question.km_range__gte = e.minValue : question.km_range__gte = null;
  e.maxValue !== 1200 ? question.km_range__lte = e.maxValue : question.km_range__lte = null;
}


const fuelEconomyHandler = (e) => {
  e.minValue !== 0 ? question.fuel_economy__gte = e.minValue : question.fuel_economy__gte = null;
  e.maxValue !== 25 ? question.fuel_economy__lte = e.maxValue : question.fuel_economy__lte = null;
}

const powerHandler = (e) => {
  e.minValue !== 0 ? question.power__gte = e.minValue : question.power__gte = null;
  e.maxValue !== 1000 ? question.power__lte = e.maxValue : question.power__lte = null;
}

const accelerationHandler = (e) => {
  e.minValue !== 0 ? question.acceleration__gte = e.minValue : question.acceleration__gte = null;
  e.maxValue !== 20 ? question.acceleration__lte = e.maxValue : question.acceleration__lte = null;
}

const engineHandler = (e) => {
  e.minValue !== 0 ? question.engine__gte = e.minValue : question.engine__gte = null;
  e.maxValue !== 9 ? question.engine__lte = e.maxValue : question.engine__lte = null;

}

watch(question, () => {
  emit('answers', {
        comfort: question.comfort,
        overallStyle: question.overall_style,
        min5YearsWarranty: question.min_5_years_warranty,
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
        powerLte: question.power__lte,
        accelerationGte: question.acceleration__gte,
        accelerationLte: question.acceleration__lte,
        engineGte: question.engine__gte,
        engineLte: question.engine__lte,
      }
  )
})
</script>
<style scoped>
:deep(.range-km.multi-range-slider .thumb .caption *:after),
:deep(.range-km.labels .label:after) {
  content: 'km';
}

:deep(.acceleration.multi-range-slider .thumb .caption *:after),
:deep(.acceleration.labels .label:after) {
  content: 'sec';
}

:deep(.power-kw.multi-range-slider .thumb .caption *:after),
:deep(.power-kw.labels .label:after) {
  content: 'kW';
}


:deep(.fuel-economy.multi-range-slider .thumb .caption *:after),
:deep(.fuel-economy.labels .label:after),
:deep(.engine.multi-range-slider .thumb .caption *:after),
:deep(.engine.labels .label:after) {
  content: 'L';
}

</style>
