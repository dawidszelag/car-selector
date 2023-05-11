<template>
  <Modal
      :cancelButton="{text: 'No', onclick: handleClickCancel, loading: true}"
         :okButton="{text: 'Yes', onclick: handleClickOk, loading: true}">
    Was the selection helpful? Yes/No
  </Modal>
</template>

<script setup lang="ts">
import {Modal} from 'usemodal-vue3';
import {CarsService} from "../api";

const emit = defineEmits(['ready'])
const handleClickOk = () => {
  CarsService.sendFeedback({feedback: true})
  emit('ready')
}

const handleClickCancel = () => {
  CarsService.sendFeedback({feedback: false})
  emit('ready')
}
</script>
<style lang="less" scoped>

:deep(.modal-vue3-header) {
  display: none;
}

:deep(.modal-vue3-content) {
  border: none !important;
  color: rgba(255, 255, 255, 0.85) !important;
  background: rgba(36, 36, 36, 0.85) !important;
  box-shadow: 0 2px 3px rgb(0 0 0 / 40%) !important;
}

:deep(.modal-vue3-footer) {
  border-top: none !important;
}


:deep(.modal-vue3-footer-ok) {
  background: linear-gradient(rgba(215, 29, 128, 0.9), rgba(196, 44, 140, 0.9)) !important;
}
</style>