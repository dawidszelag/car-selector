<template>
  <div>
    <question-label
        number="6"
        help-text="- select all that apply"
        question="Which body type(s) would you like?"/>
    <div class="answers-box-no-margin select-boxes">
      <image-box v-for="body in bodies"
                 :key="body.id"
                 :name="body.name"
                 :img="body.thumbnail"
                 :selected="bodiesIds.includes(body.id)"
                 :margin-top="-10"
                 @click="toggleBodies(body.id)"
      />
    </div>
    <div class="answers-box answers-box-no-margin">
      <checkout-field v-model="question.unsure" label="unsure"/>
      <checkout-field v-model="question.doesnt_matter" label="doesn't matter"/>
    </div>
  </div>
</template>

<script setup>
import {reactive, defineEmits, defineProps, ref, watch} from "vue";
import QuestionLabel from "../QuestionLabel";

import CheckoutField from "../CheckoutField";
import ImageBox from "../ImageBox";

defineProps({
  bodies: {
    type: Array,
    required: true
  }
})
const emit = defineEmits(['answers'])
const bodiesIds = ref([])
const question = reactive({
  unsure: null,
  doesnt_matter: null,
})
watch(() => question.doesnt_matter, () => {
  if (question.doesnt_matter) {
    question.unsure = null;
    bodiesIds.value = [];
    emit("answers", {bodiesIdIn: bodiesIds.value})
  }


})

watch(() => question.unsure, () => {
  if (question.unsure) {
    question.doesnt_matter = null
    bodiesIds.value = []
    emit("answers", {bodiesIdIn: bodiesIds.value})
  }

})

const toggleBodies = (brandId) => {
  if (bodiesIds.value.includes(brandId)) {
    bodiesIds.value = bodiesIds.value.filter(item => {
      return item !== brandId;
    })
  } else {
    question.doesnt_matter = null;
    question.unsure = null;
    bodiesIds.value.push(brandId)
  }
  emit("answers", {bodiesIdIn: bodiesIds.value})
}

</script>
<style scoped>
.answers-box-no-margin {
  margin-left: 0;
}
</style>
