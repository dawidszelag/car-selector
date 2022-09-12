<template>
  <input
      class="field"
      :id="uniqueId"
      type="checkbox"
      :checked="modelValue"
      :value="modelValue"
      @input="handleInput"
  />
  <label :for="uniqueId"> <span>{{ label }}</span></label>
</template>

<script setup>
import {defineProps} from "vue";
import {v4 as uuidv4} from "uuid";

const uniqueId = uuidv4();

const emit = defineEmits(['update:modelValue'])
defineProps(['modelValue', 'label'])

const handleInput = (event) => {
  let emitValue = null;
  if (event.target.value === 'on') emitValue = true;
  emit('update:modelValue', emitValue)
}
</script>

<style scoped>
.field[type="checkbox"]:not(:checked),
.field[type="checkbox"]:checked {
  height: 0;
  opacity: 0;
}


.field[type="checkbox"]:not(:checked) + label,
.field[type="checkbox"]:checked + label {
  position: relative;
  padding: 7px 15px;
  font-size: 15px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.85);
  cursor: pointer;
  background: rgba(0, 0, 0, 0.2);
  margin: 2px 0;
  margin-left: 30px;
  max-width: 350px;
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
}

/* checkbox aspect */
.field[type="checkbox"]:not(:checked) + label:before,
.field[type="checkbox"]:checked + label:before {
  content: '';
  position: absolute;
  left: -42px;
  top: 0;
  width: 37px;
  height: 34px;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
}

/* checked mark aspect */
.field[type="checkbox"]:not(:checked) + label:after,
.field[type="checkbox"]:checked + label:after {
  content: '✕';
  position: absolute;
  top: 18px;
  left: -28px;
  font-size: 12px;
  font-weight: 900;
  color: #fff;
  line-height: 0;
  transition: all .2s;
}


.field[type="checkbox"]:not(:checked) + label:hover,
.field[type="checkbox"]:not(:checked) + label:hover:before,
.field[type="checkbox"]:checked + label,
.field[type="checkbox"]:checked + label:after,
.field[type="checkbox"]:checked + label:before {
  background: rgba(255, 255, 255, 0.1);
}

.field[type="checkbox"]:checked + label:before {
  background: linear-gradient(#d71d80, #c42c8c) rgba(176, 30, 30, 0.3);
}

/* checked mark aspect changes */
.field[type="checkbox"]:not(:checked) + label:after {
  opacity: 0;
  transform: scale(0) rotate(45deg);
}

.field[type="checkbox"]:checked + label:after {
  opacity: 1;
  transform: scale(1) rotate(0);
}

/* Disabled checkbox */
.field[type="checkbox"]:disabled:not(:checked) + label:before,
.field[type="checkbox"]:disabled:checked + label:before {
  box-shadow: none;
  border-color: #bbb;
  background-color: #e9e9e9;
}

.field[type="checkbox"]:disabled:checked + label:after {
  color: #777;
}

.field[type="checkbox"]:disabled + label {
  color: #aaa;
}

/* End disabled checkbox */

</style>