<template>
  <div>
    <question-label
        number="7"
        help-text="- select all that apply"
        question="What car size would you like?"/>
    <div class="answers-box">
      <checkout-field v-model="question.compact" label="compact"/>
      <checkout-field v-model="question.medium" label="medium"/>
      <checkout-field v-model="question.large" label="large"/>
      <checkout-field v-model="question.unsure" label="unsure"/>
      <checkout-field v-model="question.doesnt_matter" label="doesn’t matter"/>
    </div>
  </div>
</template>

<script setup>
import {reactive, watch} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckboxField";

const emit = defineEmits(['answers'])
const question = reactive({
  compact: null,
  medium: null,
  large: null,
  unsure: null,
  doesnt_matter: null,
})


watch(() => question.unsure, () => {
      if (question.unsure) {
        question.compact = null;
        question.medium = null;
        question.large = null;
        question.doesnt_matter = null;
      }
    }
)

watch(() => question.doesnt_matter, () => {
      if (question.doesnt_matter) {
        question.compact = null;
        question.medium = null;
        question.large = null;
        question.unsure = null;
      }
    }
)

watch(() => [question.compact, question.medium, question.large], () => {
      if (question.compact || question.medium || question.large) {
        question.unsure = null;
        question.doesnt_matter = null;
      }
      emit('answers', {
        compact: question.compact,
        medium: question.medium,
        large: question.large,
      })
    }
)
</script>
