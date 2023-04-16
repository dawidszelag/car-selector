<template>
  <div class="box"
       :class="{'box--selected': selected}">
    <div style="line-height: 0">
      <img :style="{'height': `${iconSize}px`}" :src="img || DefaultIcon" :alt="name">
    </div>
    <div class="break" :style="{'marginTop': `${marginTop}px`}">{{ name }}</div>
  </div>
</template>

<script setup>
import {defineProps} from "vue";
import DefaultIcon from "@/assets/default-icon.png"

defineProps({
  name: {
    type: String,
    required: true
  },
  img: {
    type: String,
    required: false
  },
  selected: {
    type: Boolean,
    required: true
  },
  iconSize: {
    type: Number,
    required: false,
    default: 70
  },
  marginTop: {
    type: Number,
    required: false,
    default: 5
  }
})

</script>

<style scoped>
.box {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  font-weight: 900;
  font-size: 10px;
  text-align: center;
  word-break: break-word;
  text-transform: uppercase;
  width: 90px;
  min-height: 90px;
  padding: 5px;
  background: rgba(0, 0, 0, 0.2);
  margin: 5px;
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
  cursor: pointer;
}

.box img {
  width: auto;
}

.box--selected {
  background: linear-gradient(to right, rgba(224, 54, 144, 0.8), rgba(159, 4, 104, 0.8)) !important;
}
</style>