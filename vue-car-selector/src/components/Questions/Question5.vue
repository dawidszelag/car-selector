<template>
  <div>
    <question-label
        number="5"
        help-text="- select all that apply"
        question="Do you have a brand in mind?"/>
    <div class="answers-box-no-margin select-boxes">
      <ImageBox v-for="brand in brands"
                 :key="brand.id"
                 :name="brand.name"
                 :img="brand.thumbnail"
                 :selected="brandsIds.includes(brand.id)"
                 :icon-size="30"
                 @click="toggleBrand(brand.id)"
      />
    </div>
    <div class="answers-box answers-box-no-margin">
      <checkout-field v-model="question.unsure" label="unsure"/>
      <checkout-field v-model="question.doesnt_matter" label="doesn't matter"/>
    </div>
  </div>
</template>

<script setup>
import {reactive, defineEmits, defineProps, ref, watch, watchEffect} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckboxField";
import ImageBox from "../ImageBox";

defineProps({
  brands: {
    type: Array,
    required: true
  }
})
const emit = defineEmits(['answers'])
const brandsIds = ref([])
const question = reactive({
  unsure: null,
  doesnt_matter: null,
})
watch(() => question.doesnt_matter, () => {
  if (question.doesnt_matter) {
    question.unsure = null;
    brandsIds.value = [];
    emit("answers", {brandsIdIn: brandsIds.value})
  }


})

watch(() => question.unsure, () => {
  if (question.unsure) {
    question.doesnt_matter = null
    brandsIds.value = []
    emit("answers", {brandsIdIn: brandsIds.value})
  }

})

const toggleBrand = (brandId) => {
  if (brandsIds.value.includes(brandId)) {
    brandsIds.value = brandsIds.value.filter(item => {
      return item !== brandId;
    })
  } else {
    question.doesnt_matter = null;
    question.unsure = null;
    brandsIds.value.push(brandId)
  }
  emit("answers", {brandsIdIn: brandsIds.value})
}

</script>
<style scoped>
.answers-box-no-margin {
  margin-left: 0;
}
</style>
