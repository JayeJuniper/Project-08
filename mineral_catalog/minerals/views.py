from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from django.db.models import Q
from django.forms.models import model_to_dict
import random, string

from .models import Mineral


MINERALS = Mineral.objects.all()

GROUPS = [
    'Silicates',
    'Oxides',
    'Sulfates',
    'Sulfides',
    'Carbonates',
    'Halides',
    'Sulfosalts',
    'Phosphates',
    'Borates',
    'Organic Minerals',
    'Arsenates',
    'Native Elements',
    'Other'
]

MORE_GROUPS = [
    'Color',
    'Crystal System',
    'Luster',
    'Crystal Habit'
]

COLOR = ['White', 'Yellow', 'Blue', 'Red', 'Green', 'Black',
         'Brown', 'Azure', 'Ivory', 'Silver', 'Purple',
         'Gray', 'Orange']

CRYSTAL_SYSTEM = ['Triclinic', 'monoclinic', 'Orthorhombic',
                  'Tetragonal', 'Hexagonal', 'Trigonal', 'Cubic']

LUSTER = ['Metallic', 'Waxy', 'Pearly', 'Silky', 'Vitreous',
          'Greasy', 'Resinous', 'Dull', 'Adamantine']

CRYSTAL_HABIT = ['Acicular', 'Bladed', 'Botryoidal', 'Capillary',
                 'Colloform', 'Columnar', 'compact', 'Cubic', 'globular',
                 'Dendritic', 'Divergent', 'Drusy', 'Arborescent',
                 'Dodecahedral', 'encrustation', 'Equant', 'Stout', 'Fibrous',
                 'Filiform', 'Foliated', 'Granular', 'Hemimorphic',
                 'Hexagonal', 'Lamellar', 'Mammillary', 'Massive',
                 'Micaceous', 'Nodular', 'Octahedral', 'Platy', 'Plumose',
                 'Prismatic', 'Pseudo-hexagonal', 'Radiating', 'Reniform',
                 'Rosette', 'lenticular', 'Sphenoid', 'Stalactitic',
                 'Stellate', 'Striated', 'Tabular', 'Tetrahedral']

def random_pk():
    pk = random.choice(MINERALS).id
    return Mineral.objects.get(pk=pk)

def mineral_list(request):
    return render(request, 'minerals/mineral_list.html', {
                        'match': MINERALS,
                        'groups': GROUPS,
                        'random_mineral': random_pk(),
                        'alphabet_list': string.ascii_uppercase,
                        'more': MORE_GROUPS,
                        })

def mineral_detail(request, pk):
    mineral = model_to_dict(get_object_or_404(Mineral, pk=pk))
    group = ''
    return render(request, 'minerals/mineral_detail.html', {
                        'mineral': mineral,
                        'group': group,
                        'groups': GROUPS,
                        'random_mineral': random_pk(),
                        'alphabet_list': string.ascii_uppercase,
                        'more': MORE_GROUPS,
                        })

def mineral_by_letter(request, letter):
    match = MINERALS.order_by('name').filter(
        Q(name__startswith=letter)|
        Q(name__startswith=letter.upper())
        )
    return render(request, 'minerals/mineral_list.html', {
                        'match': match,
                        'group': letter,
                        'groups': GROUPS,
                        'random_mineral': random_pk(),
                        'alphabet_list': string.ascii_uppercase,
                        'more': MORE_GROUPS,
                        })

def mineral_by_group(request, group):
    match = MINERALS.order_by('name').filter(Q(group__icontains=group))
    return render(request, 'minerals/mineral_list.html', {
                        'match': match,
                        'group': group,
                        'groups': GROUPS,
                        'random_mineral': random_pk(),
                        'alphabet_list': string.ascii_uppercase,
                        'more': MORE_GROUPS,
                        })

def mineral_more(request, group):
    if group == 'Color':
        match = COLOR
    elif group == 'Crystal System':
        match = CRYSTAL_SYSTEM
    elif group == 'Luster':
        match = LUSTER
    elif group == 'Crystal Habit':
        match = CRYSTAL_HABIT
    return render(request, 'minerals/mineral_more.html', {
                        'match': match,
                        'group': group,
                        'groups': GROUPS,
                        'random_mineral': random_pk(),
                        'alphabet_list': string.ascii_uppercase,
                        'more': MORE_GROUPS,
                        })

def special_search(request, special, group):
    if group == 'Color':
        match = Mineral.objects.filter(Q(color__icontains=special))
    elif group == 'Crystal System':
        match = Mineral.objects.filter(Q(crystal_system__icontains=special))
    elif group == 'Luster':
        match = Mineral.objects.filter(Q(luster__icontains=special))
    elif group == 'Crystal Habit':
        match = Mineral.objects.filter(Q(crystal_habit__icontains=special))
    else:
        match = None
    return render(request, 'minerals/mineral_list.html', {
                    'match': match,
                    'group': group,
                    'groups': GROUPS,
                    'random_mineral': random_pk(),
                    'alphabet_list': string.ascii_uppercase,
                    'more': MORE_GROUPS,
                    'special': special
                    })

def search(request):
    query = request.GET.get('q')
    results = Mineral.objects.filter(
        Q(id__icontains=query) |
        Q(name__icontains=query) |
        Q(category__icontains=query) |
        Q(color__icontains=query) |
        Q(crystal_system__icontains=query) |
        Q(luster__icontains=query) |
        Q(streak__icontains=query) |
        Q(diaphaneity__icontains=query) |
        Q(optical_properties__icontains=query) |
        Q(crystal_habit__icontains=query) |
        Q(group__icontains=query)
        )
    return render(request, 'minerals/mineral_search.html', {
                    'results': results,
                    'query': query,
                    'groups': GROUPS,
                    'random_mineral': random_pk(),
                    'alphabet_list': string.ascii_uppercase,
                    'more': MORE_GROUPS,
                    })