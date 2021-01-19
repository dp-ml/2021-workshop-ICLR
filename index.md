---
layout: workshop      # DON'T CHANGE THIS.
# More detailed instructions (including how to fill these variables for an
# online workshop) are available at

venue: "Distributed and Private Machine Learning (DPML)"        # brief name of the institution that hosts the workshop without address (e.g., "Euphoric State University")
address: "ICLR 2021"      # full street address of workshop (e.g., "Room A, 123 Forth Street, Blimingen, Euphoria"), videoconferencing URL, or 'online'
humandate: "ICLR Workshop, May 08, 2021"    # human-readable dates for the workshop (e.g., "Feb 17-18, 2020")


eventbrite:           # optional: alphanumeric key for Eventbrite registration, e.g., "1234567890AB" (if Eventbrite is being used)
---

{% comment %} See instructions in the comments below for how to edit specific sections of this workshop template. {% endcomment %}

{% comment %}
HEADER

Edit the values in the block above to be appropriate for your workshop.
If the value is not 'true', 'false', 'null', or a number, please use
double quotation marks around the value, unless specified otherwise.
And run 'make workshop-check' *before* committing to make sure that changes are good.
{% endcomment %}


{% comment %}
Check SWC curriculum
{% endcomment %}

{% if site.carpentry == "swc" %}
{% unless site.curriculum == "swc-inflammation" or site.curriculum == "swc-gapminder" %}
<div class="alert alert-warning">
It looks like you are setting up a website for a Software Carpentry curriculum but you haven't specified the curriculum type in the <code>_config.yml</code> file (current value in <code>_config.yml</code>: "<strong>{{ site.curriculum }}</strong>", possible values: <code>swc-inflammation</code>, or <code>swc-gapminder</code>). After editing this file, you need to run <code>make serve</code> again to see the changes reflected.
</div>
{% endunless %}
{% endif %}

{% comment %}
EVENTBRITE

This block includes the Eventbrite registration widget if
'eventbrite' has been set in the header.  You can delete it if you
are not using Eventbrite, or leave it in, since it will not be
displayed if the 'eventbrite' field in the header is not set.
{% endcomment %}
{% if page.eventbrite %}
<strong>Some adblockers block the registration window. If you do not see the
  registration box below, please check your adblocker settings.</strong>
<iframe
  src="https://www.eventbrite.com/tickets-external?eid={{page.eventbrite}}&ref=etckt"
  frameborder="0"
  width="100%"
  height="280px"
  scrolling="auto">
</iframe>
{% endif %}


<h2 id="general">Scope</h2>

{% comment %}
INTRODUCTION

Edit the general explanatory paragraph below if you want to change
the pitch.
{% endcomment %}
{% if site.carpentry == "swc" %}
{% include swc/intro.html %}
{% elsif site.carpentry == "dc" %}
{% include dc/intro.html %}
{% elsif site.carpentry == "lc" %}
{% include lc/intro.html %}
{% endif %}

The focus of this workshop is to bring together researchers from industry and academia that focus on both distributed and private machine learning. These topics are of increasingly large commercial and policy interest. It is therefore important to build a community for this research area, which collaborating researchers that share insights, code, data, benchmarks, training pipelines, etc and together aim to advance distributed and private machine learning.The scope of this workshops includes, but is not limited to:

<li> Special track: privacy of ML and data in COVID-19 era </li>
<li> Distributed Machine Learning </li>
<li> Federated Learning and Split Learning</li>
<li> Differential Privacy in Deep Learning</li>
<li> Privacy and security attacks (Model Inversion, Membership Inference etc.)</li>
<li> Practical Considerations for Distributed Learning (Communication Efficiency, Compression)</li>
<li> Model and data fingerprinting/watermarking methods</li>
<li> Non i.i.d, sequential and online distributed learning</li>
<li> Differential privacy and other statistical notions of privacy: theory, applications, and implementations</li>
<li> Secure multi-party computation (Secure MPC) methods for ML</li>
<li> Homomorphic encryption for ML</li>
<li> Hardware-based techniques to privacy-preserving ML</li>
<li> Trade-offs between privacy and utility</li>
<li> Correspondence between different notions of privacy</li>
<li> Policy and Compliance for Data Privacy</li>
<li> Privacy applications in the real world ( including but not limited to Autonomous Systems, Social Networks)</li>
<li> Privacy, Fairness, Accountability and Transparency (F.A.T) in Machine Learning</li>




{% comment %}
ACCESSIBILITY

Modify the block below if there are any barriers to accessibility or
special instructions.
{% endcomment %}
<p id="accessibility">
  <strong>Accessibility:</strong>
  We are committed to making this workshop
  accessible to everybody. Please
  notify the organizers in advance of the workshop if you require any accommodations or if there is
  anything we can do to make this workshop more accessible to you.
</p>

{% comment %}
CONTACT EMAIL ADDRESS

Display the contact email address set in the configuration file.
{% endcomment %}
<p id="contact">
  <strong>Contact:</strong>
  Please email
  {% if page.email %}
  {% for email in page.email %}
  {% if forloop.last and page.email.size > 1 %}
  or
  {% else %}
  {% unless forloop.first %}
  ,
  {% endunless %}
  {% endif %}
  <a href='mailto:{{email}}'>{{email}}</a>
  {% endfor %}
  {% else %}
  dp-ml@gmail.com
  {% endif %}
  for more information.
</p>



{% comment %}
WHO CAN ATTEND?

If you would like to specify who can attend the workshop,
you can use the section below.

Move the 'endcomment' tag above the beginning of the following
<p> tag to make this section visible.

Edit the text to match who can attend the workshop. For instance:
- This workshop is open to affiliates to ABC university.
- This workshop is open to the public.
- If you are interested in attending this workshop, contact me@example.com
  for more information

<p id="who-can-attend">
    <strong>Who can attend?:</strong>
    This workshop is open to ....
</p>
{% endcomment %}

<hr/>

{% comment%}
CODE OF CONDUCT
{% endcomment %}
<h2 id="code-of-conduct">Code of Conduct</h2>

<p>
Everyone who participates in this workshop is required to conform to the <a href="https://iclr.cc/public/CodeOfConduct">ICLR Code of Conduct</a>. 
</p>


<hr/>


{% comment %}
Collaborative Notes

If you want to use an Etherpad, go to

https://pad.carpentries.org/YYYY-MM-DD-site

where 'YYYY-MM-DD-site' is the identifier for your workshop,
e.g., '2015-06-10-esu'.

Note we also have a CodiMD (the open-source version of HackMD)
available at https://codimd.carpentries.org
{% endcomment %}
{% if page.collaborative_notes %}
<h2 id="collaborative_notes">Collaborative Notes</h2>

<p>
We will use this <a href="{{ page.collaborative_notes }}">collaborative document</a> for chatting, taking notes, and sharing URLs and bits of code.
</p>
<hr/>
{% endif %}

<h3 id="general">Paper Submission</h3>
The deadline for submitting papers is February 25th, 2021. The paper format should be the same is ICLR 2021 format, and we will soon share the link for the submission website. 

<h2 id="surveys">Invited Speakers</h2>

David Evans (University of Virginia)

Lalitha Sankar (Associate Prof. ASU, Confirmed)

Gauri Joshi (Carnegie Mellon University)

Graham Cormode (University of Warwick)

<hr/>

{% comment %}
Organizers and PC Members
{% endcomment %}
<h2 id="surveys">Organizers</h2>

Adam Smith (Boston University)

Ramesh Raskar (MIT)

Jayashree Kalpathy-Cramer (Harvard)

Gautam Kamath (University of Waterloo)

Reza Shokri (NUS)

Hamed Haddadi (Imperial College London)

Vivek Sharma (MIT, Harvard, KIT)

Fatemehsadat Mireshghallah (PhD Student, UCSD)

Praneeth Vepakomma (PhD Student, MIT)

Ayush Chopra (PhD Student, MIT)

Abhishek Singh (PhD Student, MIT)


{% comment %}
Organizers and PC Members
{% endcomment %}
<h2 id="surveys">PC Members</h2>

Gauri Joshi (CMU)

Clément Canonne (University of Sydney)

Peter Kairouz (Google)

Ling Liu (GaTech)

Lin Zhong (Yale)

Arya Mazumdar (UMass Amherst)

Konstantinos Chatzikokolakis (University of Athens)

Vishnu Boddeti (Michigan State University)

Mehdi Bennis (University of Oulu)

Waheed Bajwa (Rutgers University)

Fragkiskos Koufogiannis (Raytheon)

Supriyo Chakraborty (IBM T.J. Watson Research Center)

Ananda Theertha Suresh (Google)

Jalaj Upadhyay (Apple)

Eugene Bagdasaryan (PhD Student, Cornell)

Sameer Wagh (Post-doc researcher, UC Berkeley)

<hr/>




{% comment %}
SCHEDULE

Show the workshop's schedule.

Small changes to the schedule can be made by modifying the
`schedule.html` found in the `_includes` folder for your
workshop type (`swc`, `lc`, or `dc`). Edit the items and
times in the table to match your plans. You may also want to
change 'Day 1' and 'Day 2' to be actual dates or days of the
week.

For larger changes, a blank template for a 4-day workshop
(useful for online teaching for instance) can be found in
`_includes/custom-schedule.html`. Add the times, and what
you will be teaching to this file. You may also want to add
rows to the table if you wish to break down the schedule
further. To use this custom schedule here, replace the block
of code below the Schedule `<h2>` header below with
`{% include custom-schedule.html %}`.
{% endcomment %}

<h2 id="schedule">Schedule</h2>

{% if site.carpentry == "swc" %}
{% include swc/schedule.html %}
{% elsif site.carpentry == "dc" %}
{% include dc/schedule.html %}
{% elsif site.carpentry == "lc" %}
{% include lc/schedule.html %}
{% endif %}

<hr/>



