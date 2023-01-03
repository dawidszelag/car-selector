<template>
  <div>
    <question-label
        number="8"
        help-text="- select all that apply"
        question="Which fuel type would you like?"/>
    <div class="answers-box">
      <checkout-field v-model="question.petrol" label="petrol"/>
      <checkout-field v-model="question.diesel" label="diesel"/>
      <checkout-field v-model="question.phev" label="plug-in hybrid petrol - PHEV"/>
      <checkout-field v-model="question.mhev" label="hybrid petrol - MHEV"/>
      <checkout-field v-model="question.electric" label="electric"/>
      <checkout-field v-model="question.unsure" label="unsure"/>
      <checkout-field v-model="question.doesnt_matter" label="doesn’t matter"/>
    </div>
    <div>

    </div>
  </div>
</template>

<script setup>
import {reactive, watch} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckboxField";

const emit = defineEmits(['answers'])
const question = reactive({
  petrol: null,
  diesel: null,
  phev: null,
  mhev: null,
  electric: null,
  unsure: null,
  doesnt_matter: null,
})


watch(() => question.unsure, () => {
      if (question.unsure) {
        question.petrol = null;
        question.diesel = null;
        question.phev = null;
        question.mhev = null;
        question.electric = null;
        question.doesnt_matter = null;
      }
    }
)

watch(() => question.doesnt_matter, () => {
      if (question.doesnt_matter) {
        question.petrol = null;
        question.diesel = null;
        question.phev = null;
        question.mhev = null;
        question.electric = null;
        question.unsure = null;
      }
    }
)

watch(() => [question.petrol, question.diesel, question.phev, question.mhev, question.electric], () => {
      if (question.petrol || question.diesel || question.phev || question.mhev || question.electric) {
        question.unsure = null;
        question.doesnt_matter = null;
      }
      emit('answers', {
        petrol: question.petrol,
        diesel: question.diesel,
        phev: question.phev,
        mhev: question.mhev,
        electric: question.electric,
      })
    }
)
</script>
