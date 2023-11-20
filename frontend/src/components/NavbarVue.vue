<template>
  <v-app-bar app>
    <v-toolbar-title>
      <div>
        <h1>Mini Project </h1>
        
        <a href="http://localhost:8000/admin/audio/audio/add" target="_blank" class="button-link">
          <button class="custom-button">Add Audio</button>
        </a>
      </div>
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
export default {

};
</script>
<style>
  a.button-link {
    text-decoration: none;
  }

  button.custom-button {
    background-color: #2196F3;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
  }
</style>
