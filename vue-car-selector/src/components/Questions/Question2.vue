<template>
  <div>
    <question-label
        number="2"
        help-text="- select all that apply"
        question="What is your age group?"/>
    <div class="answers-box">
      <checkout-field v-model="question.youngDriver" label="16-23"/>
      <checkout-field v-model="question.driver2345" label="23-45"/>
      <checkout-field v-model="question.middleAgedDriver" label="45-65"/>
      <checkout-field v-model="question.olderDriver" label="65+"/>
    </div>
  </div>
</template>

<script setup>
import {reactive, watch} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckboxField";

const emit = defineEmits(['answers'])
const question = reactive({
  youngDriver: null,
  driver2345: null,
  middleAgedDriver: null,
  olderDriver: null
})
watch(question, () => {
  emit('answers', question)
})

</script>
