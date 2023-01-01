<template>
  <div>
    <question-label
        number="11"
        help-text="- select all that apply"
        question=" Who will be your passenger(s)?"/>
    <div class="answers-box">
      <checkout-field v-model="question.solo_drive" label="no passengers - I drive solo"/>
      <checkout-field v-model="question.flexible" label="unsure"/>

      <div class="section-text"> NEXT TO ME:</div>
      <checkout-field v-model="question.adult" label="adult"/>
      <checkout-field v-model="question.child" label="child (without a child seat)"/>
      <checkout-field v-model="question.elderly_front_seat" label="an elderly"/>

      <div class="section-text"> BACK SEAT:</div>
      <checkout-field v-model="question.children_1" label="1 or 2 children in child seat(s)"/>
      <checkout-field v-model="question.regularly_plus_one_adult" label="1 or 2 adults"/>
      <checkout-field v-model="question.children_2" label="1 or 2 children"/>
      <checkout-field v-model="question.three_adults_back_seat" label="3 adults"/>
      <checkout-field v-model="question.elderly_back_seat" label="1 or 2 elderly"/>


      <div class="section-text"> BOOT:</div>
      <checkout-field  v-model="question.dogs" label="large dog(s)"/>
    </div>
    <div>

    </div>
  </div>
</template>

<script setup>
import {reactive, watch} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckoutField";

const emit = defineEmits(['answers'])
const question = reactive({
  solo_drive: null,
  flexible: null,
  adult: null,
  child: null,
  elderly_front_seat: null,
  children: null,
  regularly_plus_one_adult: null,
  three_adults_back_seat: null,
  elderly_back_seat: null,
  dogs: null,
})


watch(question, () => {
  emit('answers', {
        flexible: question.flexible,
        elderlyFrontSeat: question.elderly_front_seat,
        children: question.children_1 || question.children_2,
        regularlyPlusOneAdult: question.regularly_plus_one_adult,
        threeAdultsBackSeat: question.three_adults_back_seat,
        elderlyBackSeat: question.elderly_back_seat,
        dogs: question.dogs,
      }
  )
})
</script>
