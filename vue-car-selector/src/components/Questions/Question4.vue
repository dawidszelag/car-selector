<template>
  <div>
    <question-label
        number="4"
        help-text="- select range"
        question="What is your budget?"/>
    <div class="answers-box" style="padding-top: 20px">
      <MultiRangeSlider
          style="max-width: 535px"
          :min="minValue"
          :max="maxValue"
          :step="1000"
          :ruler="false"
          :label="false"
          :minValue="minValue"
          :maxValue="maxValue"
          @input="valueHandler"
      />
    </div>
  </div>
</template>

<script setup>
import {reactive, defineEmits, defineProps} from "vue";
import QuestionLabel from "../QuestionLabel";
import MultiRangeSlider from "multi-range-slider-vue";

const emit = defineEmits(['answers'])
const props = defineProps(['minValue', 'maxValue'])

const question = reactive({
  priceAuGte: null,
  priceAuLte: null,
  priceNzGte: null,
  priceNzLte: null,
})

const valueHandler = (e) => {
  e.minValue !== props.minValue ? question.priceAuGte = e.minValue : question.priceAuGte = null;
  e.maxValue !== props.maxValue ? question.priceAuLte = e.maxValue : question.priceAuLte = null;
  e.minValue !== props.minValue ? question.priceNzGte = e.minValue : question.priceNzGte = null;
  e.maxValue !== props.maxValue ? question.priceNzLte = e.maxValue : question.priceNzLte = null;
  emit("answers", question)
}


</script>
<style scoped>
:deep(.multi-range-slider .thumb .caption *:before),
:deep(.labels .label:before) {
  content: '$';
}

</style>
