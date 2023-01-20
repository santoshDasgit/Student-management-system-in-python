{% extends "header.html" %}
{% load static %}
{% block body %}

<section class='index my-3 '>
    <div class="row admin ">
        <div class="col-6 col-md-8">
            <h1>Student</h1>

            <span>
                <span>Student / <span class="text-secondary">Student list</span></span>
            </span>

        </div>
        <div class="col-6 col-md-2 mt-3 ">
            <a href="{% url 'add_student' %}" class="btn btn-warning"> add students <i class="fas fa-plus"></i></a>

        </div>
    </div>
</section>




<section class='student_list'>



    <div class="row">
        <div class="col-sm-12">
            <div class="card card-table">
                <div class="card-body">
                    <span class='text-success border border-success p-1'>Total result : {{data.count}}</span>
                   
                    <div class="table-responsive">
                        <div id="DataTables_Table_0_wrapper" class="dataTables_wrapper dt-bootstrap4 no-footer">
                            <div class="row">
                                <div class="col-sm-12 col-md-6">
                                    <div class="row">
                                        <div class="col-5">
                                            <input class="form-control my-2" id='search_input' type="search"
                                                placeholder="Search or filter" aria-label="Search">


                                        </div>
                                    </div>

                                </div>
                                <div class="col-sm-12 col-md-6"></div>
                            </div>
                            <div class="row">
                                <div class="col-sm-12">
                                    <table class="table table-hover table-center mb-0 datatable dataTable no-footer"
                                        id="DataTables_Table_0" role="grid" aria-describedby="DataTables_Table_0_info">
                                        <thead>
                                            <tr role="row">
                                                <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0"
                                                    rowspan="1" colspan="1"
                                                    aria-label="ID: activate to sort column ascending"
                                                    style="width: 45.125px;">ID</th>
                                                <th class="sorting_asc" tabindex="0" aria-controls="DataTables_Table_0"
                                                    rowspan="1" colspan="1"
                                                    aria-label="Name: activate to sort column descending"
                                                    style="width: 172.9px;" aria-sort="ascending">Name</th>
                                                <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0"
                                                    rowspan="1" colspan="1"
                                                    aria-label="Class: activate to sort column ascending"
                                                    style="width: 42.2125px;">Semistar</th>
                                                <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0"
                                                    rowspan="1" colspan="1"
                                                    aria-label="Class: activate to sort column ascending"
                                                    style="width: 42.2125px;">Branch</th>
                                                <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0"
                                                    rowspan="1" colspan="1"
                                                    aria-label="Class: activate to sort column ascending"
                                                    style="width: 42.2125px;">Course</th>
                                                <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0"
                                                    rowspan="1" colspan="1"
                                                    aria-label="Class: activate to sort column ascending"
                                                    style="width: 42.2125px;">Session Year</th>
                                                <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0"
                                                    rowspan="1" colspan="1"
                                                    aria-label="DOB: activate to sort column ascending"
                                                    style="width: 74.825px;">Email</th>
                                                <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0"
                                                    rowspan="1" colspan="1"
                                                    aria-label="DOB: activate to sort column ascending"
                                                    style="width: 74.825px;">DOB</th>
                                                <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0"
                                                    rowspan="1" colspan="1"
                                                    aria-label="Parent Name: activate to sort column ascending"
                                                    style="width: 102.2px;">Student ph </th>







                                                <th class="text-end sorting" tabindex="0"
                                                    aria-controls="DataTables_Table_0" rowspan="1" colspan="1"
                                                    aria-label="Action: activate to sort column ascending"
                                                    style="width: 74.15px;">Action</th>
                                            </tr>
                                        </thead>
                                        <tbody>

                                            

                                            {% for i in data %}
                                            <tr role="row" class="odd">

                                                <td class="">{{i.admin.username}}</td>
                                                <td class="sorting_1">
                                                    <h2 class="table-avatar">
                                                        <a href="{% url 'student_details' i.pk %}"
                                                            class="avatar avatar-sm me-2">

                                                            <img class="avatar-img rounded-circle mr-1" height="40px"
                                                                width="40px" src="
                                                            {% if i.admin.profile_image %}
                                                            {{i.admin.profile_image.url}}
                                                            {% else %}
                                                            {% static 'default_dp.jpg' %}
                                                            {% endif %}
                                                            " alt="lode">{{i.admin.first_name}}
                                                            {{i.admin.last_name}}</a>
                                                    </h2>
                                                </td>
                                                <td>
                                                    
                                                    {% if i.semester is null %}
                                                    <span class="text-danger">Not mention</span>
                                                    {% else %}
                                                    {{i.semester.name}}
                                                    {% endif %}

                                                </td>
                                                <td> {% if i.branch is null %}<span class="text-danger">Not mention</span>{% endif %} {{i.branch.name}} </td>
                                                <td> {% if i.course is null %}<span class="text-danger">Not mention</span>{% endif %} {{i.course.name}}</td>
                                                <td> {% if i.session is null %}<span class="text-danger">Not mention</span> {% else %}  {{i.session.session_start}} to {{i.session.session_end}} {% endif %} </td>
                                                <td> {% if not i.admin.email  %}<span class="text-danger">Not mention</span> {% endif %} {{i.admin.email}}</td>
                                                <td>{% if i.dob %}
                                                    {{i.dob}}
                                                    {% else %}
                                                    NULL
                                                    {% endif %} </td>
                                                <td>{% if i.ph %}
                                                    {{i.ph}}
                                                    {% else %}
                                                    NULL
                                                    {% endif %} </td>



                                                <td class="text-end">
                                                    <div class="actions">
                                                        <a href="{% url 'student_update' i.pk %}"
                                                            class="btn btn-sm btn-warning bg-success-light me-2">
                                                            <i class="fas fa-pen"></i>
                                                        </a>
                                                        <button type="button"
                                                            class="btn btn-sm bg-danger-light btn-danger myBtn" >
                                                            <i class="fas fa-trash"></i>
                                                        </button>
                                                            <!-- Remove Dropbox  -->
                                                        <div id="myModal" class="modals">

                                                            <!-- Modal content -->
                                                            <div class="modal-contents">
                                                                <span class="close">&times;</span>
                                                                <p>Conform To removed student</p>
                                                                <a href="{% url 'student_remove' i.admin.id %}" class="btn btn-danger"> Remove</a>
                                                            </div>
                                                    
                                                        </div>
                                                        
                                                    </div>
                                                </td>

                                            </tr>


                                            {% endfor %}




                                        </tbody>
                                        
                                    </table>
                                    <div class='py-3'>
                                 
 {# the current page number #}
                                        
                                       

                                    {% comment %} {% for i in count %}
                                    <p>{{i}}</p>
                                    {% endfor %} {% endcomment %}
                                    <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
                                       

                                       
                                      

                                      <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
                                        {%if data.has_previous %} {# whether the previous page exists #}
                                        <a href="?page={{data.previous_page_number}}" class='btn btn-sm btn-outline-primary'>previous</a> {# link to the prev page #}
                                    {% endif %}
                                    <span class='btn btn-sm btn-outline-primary'>{{data.number}}</span>
                                        {%if data.has_next %} {# whether the next page exists #}
                                            <a href="?page={{data.next_page_number}}" class='btn btn-sm btn-outline-primary'>Next</a> {# link to the next page #}
                                        {% endif %}
                                      
                                        <div class="btn-group" role="group">
                                          <button id="btnGroupDrop1" type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                           Switch page
                                          </button>
                                          <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
                                            {% for i in count  %}
                                            <a class="dropdown-item" href="?page={{i}}" >{{i}}</a>
                                            {% endfor %}
                                         
                                        
                                          </div>
                                        </div>
                                      </div>
                                    </div>
                                </div>
                            </div>

                         
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>





    {% comment %} search form session {% endcomment %}
    <div class="search_sec">
        <form action="" method="post">
            {% csrf_token %}
            <div class="search">
                <input type="text" name="search" placeholder="username or reg" id="">
            </div>
            <div class="filter my-2">
                <select name="branch" id="">
                    <option value="">Branch</option>
                    {% for i in branch %}
                    <option value="{{i.id}}">{{i.name}}</option>
                    {% endfor %}
                </select>

                <select name="course" id="">
                    <option value="">Course</option>
                    {% for i in course %}
                    <option value="{{i.id}}">{{i.name}}</option>
                    {% endfor %}
                </select>

                <select name="sem" id="">
                    <option value="">Sem</option>
                    {% for i in sem %}
                    <option value="{{i.id}}">{{i.name}}</option>
                    {% endfor %}
                </select>

                <select name="year" id="">
                    <option value="">Year</option>
                    {% for i in year %}

                    <option value="{{i.id}}">{{i.session_start}} to {{i.session_end}}</option>
                    {% endfor %}
                </select>
            </div>
            <div class="find">
                <input type="submit" class='btn btn-primary' value='Search'>
            </div>
        </form>
    </div>


    
  <!-- Delate conform  -->
  


</section>


{% endblock body %}