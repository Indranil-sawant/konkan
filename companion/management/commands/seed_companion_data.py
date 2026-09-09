from django.core.management.base import BaseCommand
from companion.models import Partner, Itinerary, ItineraryDay, ItineraryStop, NFCTag, EmergencyContact
from destinations.models import Destination


class Command(BaseCommand):
    help = "Seed initial NFC tags, itineraries, stops, partners, and emergency contacts for Ratnagiri"

    def handle(self, *args, **options):
        self.stdout.write("Seeding Ratnagiri Companion data...")

        # 1. Emergency Contacts
        contacts_data = [
            {
                'name': 'Ratnagiri District Civil Hospital (24x7)',
                'category': 'HOSPITAL',
                'phone_number': '+91 2352 222333',
                'alternate_phone': '108',
                'address': 'Jail Road, Near District Court, Ratnagiri, Maharashtra 415612',
                'latitude': 16.9934,
                'longitude': 73.3056,
                'is_24x7': True,
                'order': 1,
            },
            {
                'name': 'Ratnagiri City Police Control Room',
                'category': 'POLICE',
                'phone_number': '112',
                'alternate_phone': '+91 2352 222222',
                'address': 'SP Office Complex, Ratnagiri, Maharashtra 415612',
                'latitude': 16.9902,
                'longitude': 73.3120,
                'is_24x7': True,
                'order': 2,
            },
            {
                'name': 'Mirya Coastal & Marine Security Police',
                'category': 'COASTAL_POLICE',
                'phone_number': '+91 2352 232100',
                'address': 'Mirya Port Road, Ratnagiri, Maharashtra',
                'latitude': 17.0210,
                'longitude': 73.2730,
                'is_24x7': True,
                'order': 3,
            },
            {
                'name': 'Emergency Medical Ambulance (Toll-Free)',
                'category': 'AMBULANCE',
                'phone_number': '108',
                'address': 'Dispatched from nearest primary health center',
                'is_24x7': True,
                'order': 4,
            },
            {
                'name': 'Maharashtra Tourism Tourist Helpline',
                'category': 'TOURIST_HELPLINE',
                'phone_number': '1800 229 930',
                'address': 'MTDC Regional Office, Ratnagiri',
                'is_24x7': False,
                'order': 5,
            },
        ]

        for c in contacts_data:
            EmergencyContact.objects.update_or_create(
                name=c['name'],
                defaults=c
            )

        # 2. Sample Partners
        partners_data = [
            {
                'business_name': 'Hotel Sea Breeze & Coastal Suites',
                'slug': 'hotel-sea-breeze',
                'partner_type': 'HOTEL',
                'short_tagline': 'Beachfront retreat overlooking the Arabian Sea in Ratnagiri.',
                'description': 'Premium oceanfront accommodation with complimentary NFC smart room guides, authentic Konkani dining, and sunset terraces.',
                'address': 'Bhatye Beach Road, Ratnagiri, Maharashtra 415612',
                'phone': '+91 98220 12345',
                'whatsapp': '+91 98220 12345',
                'website': 'https://example.com/sea-breeze',
                'latitude': 16.9750,
                'longitude': 73.2920,
                'is_verified': True,
                'is_featured': True,
            },
            {
                'business_name': 'Atithi Parinay Heritage Homestay',
                'slug': 'atithi-parinay-homestay',
                'partner_type': 'HOMESTAY',
                'short_tagline': 'Eco-friendly traditional Konkani courtyard stay.',
                'description': 'Experience traditional red-laterite architecture, farm-fresh Ukadiche Modak, and tranquil coconut groves in Kotawade village.',
                'address': 'Kotawade, Near Ganpatipule, Ratnagiri 415617',
                'phone': '+91 98230 54321',
                'whatsapp': '+91 98230 54321',
                'latitude': 17.0850,
                'longitude': 73.3100,
                'is_verified': True,
                'is_featured': True,
            },
            {
                'business_name': 'Chaitanya Authentic Malvani Kitchen',
                'slug': 'chaitanya-malvani-kitchen',
                'partner_type': 'RESTAURANT',
                'short_tagline': 'Legendary Surmai thalis, Crab masala & Solkadhi.',
                'description': 'Celebrated local dining spot for fresh catch of the day, authentic Kokani home masalas, and refreshing Solkadhi.',
                'address': 'Main Market Road, Near Mandvi Beach, Ratnagiri',
                'phone': '+91 2352 271234',
                'latitude': 16.9880,
                'longitude': 73.2950,
                'is_verified': True,
                'is_featured': True,
            }
        ]

        partner_objs = {}
        for p in partners_data:
            obj, _ = Partner.objects.update_or_create(
                slug=p['slug'],
                defaults=p
            )
            partner_objs[p['slug']] = obj

        # 3. Curated Itineraries
        dest_map = {d.title.lower(): d for d in Destination.objects.all()}

        itineraries_data = [
            {
                'title': '2-Day Essential Ratnagiri (Forts, Beaches & Food Trail)',
                'slug': 'ratnagiri-2-day',
                'tagline': 'The quintessential Konkan weekend: Ratnadurg Fort, pristine Bhatye Beach, Thiba Palace, and fresh seafood.',
                'description': 'The ultimate introduction to Ratnagiri. Designed for weekend travelers arriving from Mumbai or Pune, covering monumental sea forts, tranquil beach sunsets, royal history, and authentic Konkani delicacies.',
                'duration_days': 2,
                'audience': 'ALL',
                'season': 'ALL',
                'difficulty': 'EASY',
                'estimated_cost_inr': '₹2,500 - ₹4,500 / person',
                'total_distance_km': 48.0,
                'is_featured': True,
                'order': 1,
                'days': [
                    {
                        'day_number': 1,
                        'title': 'Sea Forts, Royal Legacies & Sunset Horizons',
                        'summary': 'Explore the dramatic walls of Ratnadurg Fort, pay homage at Bhagwati Temple, and watch the crimson sun sink into the Arabian Sea at Bhatye Beach.',
                        'stops': [
                            {
                                'custom_title': 'Ratnadurg Fort & Bhagwati Temple',
                                'stop_type': 'FORT',
                                'order_index': 1,
                                'start_time': '08:30 AM',
                                'duration_minutes': 90,
                                'activity_description': 'Walk along the laterite ramparts surrounded on three sides by the turquoise Arabian Sea. Visit the serene Bhagwati temple inside the fort citadel.',
                                'travel_note_to_next': '10 min scenic drive down to the lighthouse',
                                'travel_time_minutes': 10,
                                'tips': 'Visit early morning to beat the coastal midday sun and catch crisp sea breezes.',
                            },
                            {
                                'custom_title': 'Ratnagiri Lighthouse & Cliff Point',
                                'stop_type': 'SIGHTSEEING',
                                'order_index': 2,
                                'start_time': '10:30 AM',
                                'duration_minutes': 45,
                                'activity_description': 'Panoramic 360-degree viewpoint looking out over Mirya Bay and fishing boats navigating the harbour mouth.',
                                'travel_note_to_next': '15 min drive to town center for lunch',
                                'travel_time_minutes': 15,
                            },
                            {
                                'custom_title': 'Authentic Malvani Seafood Lunch (Surmai Thali & Solkadhi)',
                                'stop_type': 'LUNCH',
                                'order_index': 3,
                                'start_time': '12:30 PM',
                                'duration_minutes': 75,
                                'activity_description': 'Feast on freshly fried Surmai or Pomfret, accompanied by warm Ghavane (rice crepes), Tisrya masala (clams), and pink Kokum Solkadhi.',
                                'travel_note_to_next': '10 min drive to Thiba Palace',
                                'travel_time_minutes': 10,
                            },
                            {
                                'custom_title': 'Thiba Palace & Cultural Gardens',
                                'stop_type': 'SIGHTSEEING',
                                'order_index': 4,
                                'start_time': '03:30 PM',
                                'duration_minutes': 60,
                                'activity_description': 'Discover the historic teakwood residence built for King Thibaw of Burma during his British internment. Enjoy the lush garden viewpoints.',
                                'travel_note_to_next': '15 min drive to Bhatye Beach',
                                'travel_time_minutes': 15,
                            },
                            {
                                'custom_title': 'Bhatye Beach Walk & Sunset Solkadhi',
                                'stop_type': 'SUNSET',
                                'order_index': 5,
                                'start_time': '05:30 PM',
                                'duration_minutes': 90,
                                'activity_description': 'Stroll along the wide silver-sand beach, sample spicy coastal chaat and hot roasted corn while watching a glowing Konkan sunset.',
                                'travel_note_to_next': 'Return to hotel / resort',
                                'travel_time_minutes': 15,
                            }
                        ]
                    },
                    {
                        'day_number': 2,
                        'title': 'Ganpatipule Coastal Drive & Mango Heritage',
                        'summary': 'Cruise along the world-famous Aare Ware Marine Drive, visit the holy Ganpatipule Temple by the surf, and purchase authentic Alphonso mango products.',
                        'stops': [
                            {
                                'custom_title': 'Aare Ware Marine Coastal Drive',
                                'stop_type': 'ADVENTURE',
                                'order_index': 1,
                                'start_time': '08:30 AM',
                                'duration_minutes': 60,
                                'activity_description': 'One of India’s most scenic coastal roads hugging towering cliffs on one side and endless blue ocean on the other.',
                                'travel_note_to_next': '20 min drive to Ganpatipule',
                                'travel_time_minutes': 20,
                            },
                            {
                                'custom_title': 'Ganpatipule Swayambhu Temple & Beach',
                                'stop_type': 'BEACH',
                                'order_index': 2,
                                'start_time': '10:30 AM',
                                'duration_minutes': 90,
                                'activity_description': 'Offer prayers at the 400-year-old deity resting right on the beach sands, then stroll the clean white-sand shoreline.',
                                'travel_note_to_next': '10 min walk to local lunch kitchen',
                                'travel_time_minutes': 10,
                            },
                            {
                                'custom_title': 'Traditional Konkani Vegetarian Feast (Ukadiche Modak)',
                                'stop_type': 'LUNCH',
                                'order_index': 3,
                                'start_time': '01:00 PM',
                                'duration_minutes': 60,
                                'activity_description': 'Savour steaming hot Ukadiche Modak filled with fresh grated coconut and jaggery, paired with fragrant Amti and rice.',
                                'travel_note_to_next': '15 min drive to local spice & mango market',
                                'travel_time_minutes': 15,
                            },
                            {
                                'custom_title': 'Local Mango Products & Cashew Shopping',
                                'stop_type': 'SHOPPING',
                                'order_index': 4,
                                'start_time': '03:30 PM',
                                'duration_minutes': 60,
                                'activity_description': 'Pick up authentic Hapus (Alphonso) pulp, Aam Papad, Phanas poli, and freshly roasted whole Konkan cashews.',
                                'travel_note_to_next': 'Departure / Railway Station',
                                'travel_time_minutes': 30,
                            }
                        ]
                    }
                ]
            },
            {
                'title': '1-Day Express Ratnagiri (Best Highlights in 8 Hours)',
                'slug': 'ratnagiri-1-day',
                'tagline': 'Have only one day? Experience the absolute best forts, food, and ocean views without rushing.',
                'description': 'Tailored specifically for day-trippers and transit travelers looking to maximize their time in Ratnagiri with precision stop timing and optimal driving routes.',
                'duration_days': 1,
                'audience': 'SOLO',
                'season': 'ALL',
                'difficulty': 'MODERATE',
                'estimated_cost_inr': '₹1,200 - ₹2,500 / person',
                'total_distance_km': 28.0,
                'is_featured': True,
                'order': 2,
                'days': [
                    {
                        'day_number': 1,
                        'title': 'Ratnagiri in 8 Hours',
                        'summary': 'From cliffside ramparts to coastal cuisine and sunset sands.',
                        'stops': [
                            {
                                'custom_title': 'Morning at Ratnadurg Fort',
                                'stop_type': 'FORT',
                                'order_index': 1,
                                'start_time': '09:00 AM',
                                'duration_minutes': 90,
                                'activity_description': 'Explore historic sea ramparts and the lighthouse vantage.',
                                'travel_time_minutes': 15,
                            },
                            {
                                'custom_title': 'Coastal Fish Thali Lunch',
                                'stop_type': 'LUNCH',
                                'order_index': 2,
                                'start_time': '12:30 PM',
                                'duration_minutes': 60,
                                'activity_description': 'Fresh pomfret / surmai fry and solkadhi in town.',
                                'travel_time_minutes': 15,
                            },
                            {
                                'custom_title': 'Thiba Palace & Heritage Walk',
                                'stop_type': 'SIGHTSEEING',
                                'order_index': 3,
                                'start_time': '02:30 PM',
                                'duration_minutes': 60,
                                'activity_description': 'Royal Burmese exile mansion & panoramic hillside view.',
                                'travel_time_minutes': 15,
                            },
                            {
                                'custom_title': 'Sunset at Mandvi Black Sand Beach',
                                'stop_type': 'SUNSET',
                                'order_index': 4,
                                'start_time': '05:00 PM',
                                'duration_minutes': 90,
                                'activity_description': 'Unique black sands and bustling evening street food stalls.',
                                'travel_time_minutes': 20,
                            }
                        ]
                    }
                ]
            },
            {
                'title': 'Family Holiday Trail (Safe Waters, Temples & Nature)',
                'slug': 'family-konkan-holiday',
                'tagline': 'Child-friendly beaches, gentle waters, rich cultural temples, and comfortable transit.',
                'description': 'A relaxed itinerary created for families with children and elders. Features accessible paved paths, safe swim zones, clean amenities, and wholesome dining.',
                'duration_days': 2,
                'audience': 'FAMILY',
                'season': 'WINTER',
                'difficulty': 'EASY',
                'estimated_cost_inr': '₹3,000 - ₹5,000 / day',
                'total_distance_km': 42.0,
                'is_featured': True,
                'order': 3,
                'days': [
                    {
                        'day_number': 1,
                        'title': 'Gentle Waters & Heritage Gardens',
                        'summary': 'Calm shores and relaxed palace gardens suited for all ages.',
                        'stops': [
                            {
                                'custom_title': 'Bhatye Beach Family Sandcastle & Walk',
                                'stop_type': 'BEACH',
                                'order_index': 1,
                                'start_time': '09:00 AM',
                                'duration_minutes': 90,
                                'activity_description': 'Flat, wide, safe beach shoreline for children to play.',
                                'travel_time_minutes': 15,
                            },
                            {
                                'custom_title': 'Thiba Palace Heritage Stroll & Picnic Lawn',
                                'stop_type': 'SIGHTSEEING',
                                'order_index': 2,
                                'start_time': '11:30 AM',
                                'duration_minutes': 60,
                                'activity_description': 'Shaded lawns and museum exhibits.',
                                'travel_time_minutes': 15,
                            }
                        ]
                    }
                ]
            },
            {
                'title': 'Couples & Romantic Sunset Trail',
                'slug': 'romantic-sunset-trail',
                'tagline': 'Cliffside sea lookouts, secluded cove walks, and quiet candlelight coastal dining.',
                'description': 'Designed for couples seeking scenic photography spots, serene horizons, and quiet moments across the Konkan coastline.',
                'duration_days': 2,
                'audience': 'COUPLE',
                'season': 'WINTER',
                'difficulty': 'EASY',
                'estimated_cost_inr': '₹3,500 - ₹6,000 / day',
                'total_distance_km': 55.0,
                'is_featured': True,
                'order': 4,
                'days': [
                    {
                        'day_number': 1,
                        'title': 'Aare Ware Clifftops & Candlelight',
                        'summary': 'Dramatic clifftop vistas over the crashing Arabian Sea waves.',
                        'stops': [
                            {
                                'custom_title': 'Aare Ware Ocean Overlook Point',
                                'stop_type': 'SUNSET',
                                'order_index': 1,
                                'start_time': '04:30 PM',
                                'duration_minutes': 90,
                                'activity_description': 'Unrivaled sunset colors casting gold across the marine bypass cliffs.',
                                'travel_time_minutes': 20,
                            }
                        ]
                    }
                ]
            },
            {
                'title': 'Taste of Ratnagiri Culinary & Mango Trail',
                'slug': 'taste-of-ratnagiri',
                'tagline': 'Malvani seafood masalas, Ukadiche Modak, Ghavane, Solkadhi, and world-renowned Alphonso mangoes.',
                'description': 'A food-lover’s expedition through bustling morning fish docks, family spice mills, authentic home thali joints, and heritage sweet shops.',
                'duration_days': 1,
                'audience': 'FOODIE',
                'season': 'ALL',
                'difficulty': 'EASY',
                'estimated_cost_inr': '₹1,500 - ₹3,000 / person',
                'total_distance_km': 25.0,
                'is_featured': True,
                'order': 5,
                'days': [
                    {
                        'day_number': 1,
                        'title': 'From Morning Ghavane to Evening Surmai',
                        'summary': 'The ultimate Konkan culinary marathon.',
                        'stops': [
                            {
                                'custom_title': 'Breakfast: Hot Ghavane & Coconut Chutney with Chaha',
                                'stop_type': 'BREAKFAST',
                                'order_index': 1,
                                'start_time': '08:30 AM',
                                'duration_minutes': 45,
                                'activity_description': 'Light, lacy rice-flour pancakes served with sweetened coconut milk.',
                                'travel_time_minutes': 10,
                            },
                            {
                                'custom_title': 'Mirya Harbour Morning Fish Auction Walk',
                                'stop_type': 'MORNING',
                                'order_index': 2,
                                'start_time': '09:45 AM',
                                'duration_minutes': 45,
                                'activity_description': 'Witness colourful trawlers bringing in kingfish, prawns, and crabs.',
                                'travel_time_minutes': 15,
                            },
                            {
                                'custom_title': 'Lunch: Surmai & Prawns Malvani Thali',
                                'stop_type': 'LUNCH',
                                'order_index': 3,
                                'start_time': '01:00 PM',
                                'duration_minutes': 75,
                                'activity_description': 'Spiced fried fish, seafood curry, rice, and double solkadhi.',
                                'travel_time_minutes': 15,
                            },
                            {
                                'custom_title': 'Dessert & Souvenirs: Mango Pulp & Cashew Tasting',
                                'stop_type': 'SHOPPING',
                                'order_index': 4,
                                'start_time': '04:00 PM',
                                'duration_minutes': 60,
                                'activity_description': 'Sample dried mango poli, cashew feni vinegar, and fresh modaks.',
                                'travel_time_minutes': 15,
                            }
                        ]
                    }
                ]
            }
        ]

        for itin_data in itineraries_data:
            days_data = itin_data.pop('days', [])
            itin_obj, _ = Itinerary.objects.update_or_create(
                slug=itin_data['slug'],
                defaults=itin_data
            )
            for d_data in days_data:
                stops_data = d_data.pop('stops', [])
                day_obj, _ = ItineraryDay.objects.update_or_create(
                    itinerary=itin_obj,
                    day_number=d_data['day_number'],
                    defaults=d_data
                )
                for s_data in stops_data:
                    ItineraryStop.objects.update_or_create(
                        day=day_obj,
                        order_index=s_data['order_index'],
                        defaults=s_data
                    )

        # 4. Sample Smart NFC Tags
        tags_data = [
            {
                'tag_uid': 'RATNA-HOTEL-01',
                'title': 'Hotel Sea Breeze - Guest Room NFC Tag',
                'tag_type': 'HOTEL',
                'target_experience': 'HOME',
                'assigned_partner': partner_objs.get('hotel-sea-breeze'),
                'custom_welcome_title': 'Welcome Guest of Hotel Sea Breeze 🌴',
                'custom_welcome_message': 'Your personal digital concierge is ready with curated itineraries, beach guides, and emergency help.',
                'tap_count': 142,
                'unique_visitor_count': 98,
            },
            {
                'tag_uid': 'RATNA-2DAY-TRIP',
                'title': '2-Day Essential Ratnagiri Itinerary Tag',
                'tag_type': 'ITINERARY',
                'target_experience': 'SPECIFIC_ITINERARY',
                'assigned_itinerary': Itinerary.objects.filter(slug='ratnagiri-2-day').first(),
                'custom_welcome_title': 'Your 2-Day Ratnagiri Journey Starts Now!',
                'custom_welcome_message': 'Follow this curated step-by-step route with live directions and dining stops.',
                'tap_count': 324,
                'unique_visitor_count': 215,
            },
            {
                'tag_uid': 'RATNA-FOOD-TRAIL',
                'title': 'Taste of Ratnagiri Food Trail Tag',
                'tag_type': 'FOOD_TRAIL',
                'target_experience': 'FOOD_TRAIL',
                'custom_welcome_title': 'Taste the Flavours of Ratnagiri 🍛',
                'custom_welcome_message': 'Discover authentic seafood, sweet mango specialties, and secret local food joints.',
                'tap_count': 89,
                'unique_visitor_count': 74,
            },
            {
                'tag_uid': 'RATNA-SOS-SAFETY',
                'title': 'Tourist SOS Emergency Assistance Tag',
                'tag_type': 'EMERGENCY',
                'target_experience': 'EMERGENCY',
                'custom_welcome_title': '1-Click Tourist Emergency & Safety Center 🚨',
                'custom_welcome_message': 'Instant telephone links to 24x7 hospitals, police control, coastal rescue, and tourist helpline.',
                'tap_count': 31,
                'unique_visitor_count': 29,
            },
            {
                'tag_uid': 'RATNA-NEAR-ME',
                'title': 'Live Radar "What\'s Near Me" Tag',
                'tag_type': 'GENERAL',
                'target_experience': 'NEAR_ME',
                'custom_welcome_title': 'Live Tourist Radar 📍',
                'custom_welcome_message': 'Detecting closest beaches, sea forts, restaurants, and fuel pumps around you.',
                'tap_count': 210,
                'unique_visitor_count': 160,
            }
        ]

        for t in tags_data:
            NFCTag.objects.update_or_create(
                tag_uid=t['tag_uid'],
                defaults=t
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded Ratnagiri NFC Tourist Companion data!"))
