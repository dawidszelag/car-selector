<template>
  <div>
    <question-label
        number="8"
        help-text="- select all that apply"
        question="Fuel type?"/>
    <div class="answers-box">
      <checkout-field v-model="question.petrol" label="petrol"/>
      <checkout-field v-model="question.diesel" label="diesel"/>
      <checkout-field v-model="question.electric" label="electric"/>
      <checkout-field v-model="question.hev" label="hybrid petrol - HEV"/>
      <checkout-field v-model="question.phev" label="plug-in hybrid petrol - PHEV"/>
      <checkout-field v-model="question.mhevPetrol" label="mild hybrid petrol - MHEV"/>
      <checkout-field v-model="question.mhevDiesel" label="mild hybrid diesel - MHEV"/>
      <checkout-field v-model="question.unsure" label="unsure"/>
      <checkout-field v-model="question.doesnt_matter" label="doesn’t matter"/>
    </div>
    <div>
    </div>
  </div>
  <Modal
      :okButton="showDieselInfo=false"
      v-model:visible="showDieselInfo">
    For short distances and local driving, diesel is not recommended. Instead, we suggest the following:
    - petrol
    - hybrid petrol - HEV
    - plug-in hybrid petrol – PHEV mild hybrid petrol - MHEV
    - electric
  </Modal>

  <Modal
      :okButton="showElectricInfo=false"
      v-model:visible="showElectricInfo">
    For long distances, an electric car is not recommended. Instead, we suggest the following:
    - petrol
    - diesel
    - hybrid petrol - HEV
    - plug-in hybrid petrol - PHEV
    - mild hybrid petrol - MHEV
    - mild hybrid diesel - MHEV
  </Modal>
</template>

<script setup>
import {reactive, ref, watch} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckboxField";
import {Modal} from "usemodal-vue3";

import {useAppStore} from "../../store";


const showDieselInfo = ref(false);
const showElectricInfo = ref(false);

const appStore = useAppStore();

const emit = defineEmits(['answers'])
const question = reactive({
  petrol: null,
  diesel: null,
  phev: null,
  hev: null,
  mhevPetrol: null,
  mhevDiesel: null,
  electric: null,
  unsure: null,
  doesnt_matter: null,
})

watch(() => question.diesel, () => {
      if (question.diesel && appStore.form?.shortDistance) {
        showDieselInfo.value = true;
      }
    }
)

watch(() => question.electric, () => {
      if (question.electric && appStore.form?.longDistance) {
        showElectricInfo.value = true;
      }
    }
)

watch(() => question.unsure, () => {
      if (question.unsure) {
        question.petrol = null;
        question.diesel = null;
        question.phev = null;
        question.hev = null;
        question.mhevPetrol = null;
        question.mhevDiesel = null;
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
        question.hev = null;
        question.mhevPetrol = null;
        question.mhevDiesel = null;
        question.electric = null;
        question.unsure = null;
      }
    }
)

watch(() => [question.petrol, question.diesel, question.hev, question.phev, question.mhevPetrol, question.mhevDiesel, question.electric], () => {
      if (question.petrol || question.diesel || question.phev || question.hev || question.mhevPetrol || question.mhevDiesel || question.electric) {
        question.unsure = null;
        question.doesnt_matter = null;
      }
      emit('answers', {
        ...question
      })
    }
)
</script>
