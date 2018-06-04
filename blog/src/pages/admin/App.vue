<template>
  <div id="app">
    <div class="article-actions">
      <router-link to="/articlewrite">写文章</router-link>
      <router-link to="/manage">文章管理</router-link>
    </div>
    <router-view></router-view>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  margin: auto;
  text-align: center;
  max-width: 900px;
}

.article-actions {
  margin-top: 30px;
}

.article-actions a {
  display: inline-block;
  padding: 6px 12px;
  margin-bottom: 0;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.42857143;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  cursor: pointer;
  user-select: none;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 4px;
  text-decoration: none;
}

.router-link-active {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}


</style>
