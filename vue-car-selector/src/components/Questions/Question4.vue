<template>
  <div>
    <question-label
        number="4"
        help-text="- select a range"
        question="What is your budget?"/>
    <div class="answers-box" style="padding-top: 20px">
      <Slider :min="minValue"
              :max="maxValue"
              :step="10000"
              :merge="100000"
              v-model="price_range.value"
              v-bind="price_range"
              class="price"/>
    </div>
  </div>
</template>

<script setup>
import {reactive, watch, defineEmits, defineProps } from "vue";
import QuestionLabel from "../QuestionLabel";
import Slider from '@vueform/slider'

const emit = defineEmits(['answers'])
const props = defineProps(['minValue', 'maxValue'])
const price_range = reactive({
  value: [props.minValue, props.maxValue]
})
const question = reactive({
  priceAuGte: null,
  priceAuLte: null,
  priceNzGte: null,
  priceNzLte: null,
})

watch(price_range, () => {
  price_range.value[0] !== props.minValue ? question.priceAuGte = price_range.value[0] : question.priceAuGte = null;
  price_range.value[1] !== props.maxValue ? question.priceAuLte = price_range.value[1] : question.priceAuLte = null;
  price_range.value[0] !== props.minValue ? question.priceNzGte = price_range.value[0] : question.priceNzGte = null;
  price_range.value[1] !== props.maxValue ? question.priceNzLte = price_range.value[1] : question.priceNzLte = null;
  emit("answers", question)
})


</script>
<style>
.price .slider-tooltip-top:after {
  content: '$';
}

</style>
